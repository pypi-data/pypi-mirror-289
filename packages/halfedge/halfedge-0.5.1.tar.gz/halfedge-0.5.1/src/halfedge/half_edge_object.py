"""The HalfEdges data structure and operations on it.

Extend StaticHalfEdges with methods that alter the mesh.

:author: Shay Hill
:created: 2024-08-05
"""

from __future__ import annotations

from contextlib import suppress
from typing import TypeVar

from paragraphs import par

from halfedge.half_edge_elements import Edge, Face, ManifoldMeshError, Vert
from halfedge.half_edge_querries import StaticHalfEdges

_T = TypeVar("_T")


def _update_face_edges(face: Face, edge: Edge) -> None:
    """Add or update face attribute for each edge in edge.face_edges.

    :param face: each edge will point to this face
    :param edge: one edge on the face (even if the edge doesn't point to the face yet)

    This is the only way to add a face to a mesh, because faces only exist as long as
    there is an edge pointing to them.
    """
    for edge_ in edge.face_edges:
        edge_.face = face


def _get_singleton_item(one: set[_T]) -> _T:
    """If a set has exactly one item, return that item.

    :param one: A set with presumably one item
    :return:
    """
    (item,) = one
    return item


class UnrecoverableManifoldMeshError(ValueError):
    """Found a problem with an operation AFTER mesh was potentially altered.

    Unexpected error. This should have been caught earlier. We found a something that
    couldn't be added or couldn't be removed, but we didn't find it in time. The mesh
    may have been altered before this discovery. We've found a bug in the module.
    """

    def __init__(self, message: str) -> None:
        """Pass message to ValueError."""
        super().__init__(self, message)


class HalfEdges(StaticHalfEdges):
    """HalfEdges data structure and operations on it."""

    def _get_edge_or_vert_faces(self, elem: Edge | Vert) -> set[Face]:
        """Get faces (unordered) adjacent to a vert or edge.

        :param elem: Vert or Edge instance
        :return: Face instances adjacent

        This is a subroutine for insert_edge.
        """
        if isinstance(elem, Edge):
            return {elem.face}
        return set(elem.faces)

    def _infer_face(self, orig: Edge | Vert, dest: Edge | Vert) -> Face:
        """Infer which face two verts lie on.

        :elem: vert or edge (presumably on the face)
        :return: face (if unambiguous) on which vert or edge lies

        Able to infer from:
            * both verts on same face: that face
            * empty mesh: a new Hole
        """
        if not self.edges:
            return self.new_hole()
        orig_faces = self._get_edge_or_vert_faces(orig)
        dest_faces = self._get_edge_or_vert_faces(dest)
        with suppress(ValueError):
            return _get_singleton_item(orig_faces & dest_faces)
        msg = "face cannot be determined from orig and dest"
        raise ValueError(msg)

    def _infer_wing(
        self, elem: Edge | Vert, face: Face, default: Edge
    ) -> tuple[Vert, Edge]:
        """Given a vert or edge, try to ret vert and edge such that edge.dest == vert.

        :param elem: vert or edge in the mesh
        :param face: face on which vert or edge lies
        :param default: edge value if vert is new (no connected edges)
            - this will always be the edge pair.
        :return: a vert on the face (or presumed to be) and the edge ENDING at vert

        This is a subroutine of insert_edge, which accepts a vert or edge as origin
        and destination arguments. The wing returned is

            * the origin of the edge to be inserted.
            * the edge *before* the edge to be inserted (the prev edge)

        elem (insert_edge orig or dest argument) is an edge: edge.dest and edge
        elem (insert_edge orig or dest argument) is a vert:

            vert on face? the prev edge is the face edge ending in vert

            vert not on face? (presume floating) the prev edge is default
                (new_edge.pair from outer scope)
        """
        if isinstance(elem, Edge):
            return elem.dest, elem
        if elem not in face.verts:
            return elem, default
        prev_edge = _get_singleton_item({x for x in face.edges if x.dest is elem})
        return elem, prev_edge

    def _point_away_from_edge(self, *edges: Edge) -> None:
        """Prepare edge to be removed. Remove vert and face pointers to edge.

        :param edge: any edge in mesh
        :effects: points edge.orig and edge.face to another edge

        Each vert and each face point to an adjacent edge. *Which* adjacent edge is
        incidental. This method tries to point an edge's origin and face to
        *something else*.

        This method requires an intact mesh and produces an intact mesh. After this
        method, the mesh will be perfectly equivalent to its previous state. However,
        this method has to be called *before* we start other preparation to remove
        the edge, because *those* preparations *will* alter the mesh and prevent
        *this* method from working.

        The method will fail silently if the edge.orig or edge.face doesn't have
        another edge to point to. But that won't matter, because that orig or face
        will go out of scope when the edge is removed.
        """
        for edge_ in edges:
            safe_vert_edges = set(edge_.vert_edges) - set(edges)
            edge_.orig.edge = next(iter(safe_vert_edges), edge_)
            safe_face_edges = set(edge_.face_edges) - set(edges)
            edge_.face.edge = next(iter(safe_face_edges), edge_)

    def insert_edge(
        self, orig: Edge | Vert, dest: Edge | Vert, face: Face | None = None
    ) -> Edge:
        """Insert a new edge between two verts.

        :param orig: origin of new edge (vert or edge such that edge.dest == vert)
        :param dest: destination of new edge (vert or edge as above)
        :param face: edge will lie on or split face (will infer if unambiguous)
        :return: newly inserted edge
        :raise ValueError: if no face is given and face is ambiguous
        :raise ValueError: if
            * overwriting existing edge
            * any vert in mesh but not on face
            * orig and dest are the same
            * edge is not connected to mesh (and mesh is not empty)

        Edge face is created.
        Pair face is retained.

        This will only split the face if both orig and dest are new Verts. This function
        will connect:

            * two existing Verts on the same face
            * an existing Vert to a new vert inside the face
            * a new vert inside the face to an existing vert
            * two new verts to create a floating edge in an empty mesh.

        Passes attributes:

            * shared face.edges attributes passed to new edge
            * face attributes passed to new face if face is split
        """
        if face is None:
            face = self._infer_face(orig, dest)

        # create a floating edge. pass attributes later
        edge = self.new_edge()
        edge.pair = self.new_edge(pair=edge, next=edge, prev=edge)

        edge_orig, edge_prev = self._infer_wing(orig, face, edge.pair)
        edge_dest, pair_prev = self._infer_wing(dest, face, edge)
        edge_next, pair_next = edge_prev.next, pair_prev.next

        if getattr(edge_orig, "edge", None) and edge_dest in edge_orig.neighbors:
            msg = "overwriting existing edge"
            raise ValueError(msg)

        edge_points_in_face = set(face.verts) & {edge_orig, edge_dest}
        edge_points_in_mesh = set(self.verts) & {edge_orig, edge_dest}
        if edge_points_in_face != edge_points_in_mesh:
            msg = "orig or dest in mesh but not on given face"
            raise ValueError(msg)

        if edge_orig == edge_dest:
            msg = "orig and dest are the same"
            raise ValueError(msg)

        if not edge_points_in_face and face in self.faces:
            msg = "adding floating edge to existing face"
            raise ValueError(msg)

        edge.orig = edge_orig
        edge.prev = edge_prev
        edge.next = pair_next

        edge.pair.orig = edge_dest
        edge.pair.prev = pair_prev
        edge.pair.next = edge_next

        # if face is not split, new face will be created then immediately written over
        new_face = self.new_face()
        _ = new_face.split_from(face)
        _update_face_edges(new_face, edge)
        _update_face_edges(face, edge.pair)

        _ = edge.merge_from(*[x for x in edge.face_edges if x not in {edge, edge.pair}])
        _ = edge.pair.merge_from(
            *[x for x in edge.pair.face_edges if x not in {edge, edge.pair}]
        )

        self.edges.update({edge, edge.pair})

        return edge

    def insert_vert(self, face: Face) -> Vert:
        """Insert a new vert into face then triangulate face.

        :param face: face to triangulate
        :returns: newly inserted vert
        :raise UnrecoverableManifoldMeshError: if a problem was found after we started
            altering the mesh (this SHOULD never happen).

        new vert is created on face
        new edges are created from new vert to extant face verts
        new faces are created as face is triangulated

        Passes attributes:

            * face attributes passed to new faces
            * shared face.edges attributes passed to new edges
            * shared face.verts attributes passed to new vert
        """
        new_vert = self.new_vert().merge_from(*face.verts)
        try:
            for vert in face.verts:
                _ = self.insert_edge(vert, new_vert, face)
        except ManifoldMeshError as exc:
            raise UnrecoverableManifoldMeshError(str(exc)) from exc
        return new_vert

    def remove_edge(self, edge: Edge) -> Face:
        """Cut an edge out of the mesh.

        :param edge: edge to remove
        :returns: Newly joined (if edge split face) face, else new face that replaces
            previously shared face.
        :raise ValueError: if edge not in mesh
        :raise ValueError: if edge is a bridge edge

        Will not allow you to break (make non-manifold) the mesh. For example,
        here's a mesh with three faces, one in each square, and a third face or
        hole around the outside. If I remove that long edge, the hole would have
        two small, square faces inside of it. The hole would point to a half edge
        around one or the other square, but that edge would just "next" around its
        own small square. The other square could never be found.
         _       _
        |_|_____|_|

        Attempting to remove such edges will raise a ManifoldMeshError.

        Always removes the edge's face and expands the pair's face (if they are
        different).

        Passes attributes:
            * shared face attributes passed to new face

        """
        if edge not in self.edges:
            msg = f"edge {id(edge)} does not exist in mesh"
            raise ValueError(msg)

        pair = edge.pair

        if edge.orig.valence > 1 and edge.dest.valence > 1 and edge.face == pair.face:
            msg = "would create non-manifold mesh"
            raise ValueError(msg)

        self._point_away_from_edge(edge, edge.pair)

        edge_face_edges = set(edge.face_edges)
        pair_face_edges = set(pair.face_edges)

        # point all edges to new face
        new_face: Face = self.new_face().merge_from(*{edge.face, pair.face})
        for edge_ in (edge_face_edges | pair_face_edges) - {edge, pair}:
            edge_.face = new_face

        # disconnect from previous edges
        edge.prev.next = pair.next
        pair.prev.next = edge.next
        self.edges -= {edge, pair}

        return new_face

    @staticmethod
    def _is_bridge(edge: Edge) -> bool:
        """Return True if edge is a bridge edge.

        :param edge: edge in mesh
        :return: True if edge is a bridge edge

        A bridge edge is an edge that, if removed, would leave a disjoint face.

        0--1  2--3
        |  |  |  |
        4--5--6--7

        Here, edge 5--6 would be a bridge edge. If it were removed, the surrounding
        face would have 8 edges and 8 verts, but not all would be connected.

        """
        return (
            edge.orig.valence > 1
            and edge.dest.valence > 1
            and edge.face is edge.pair.face
        )

    @staticmethod
    def _is_peninsula(edge: Edge) -> bool:
        """Return True if edge is a peninsula edge.

        :param edge: edge in mesh
        :return: True if edge is a peninsula edge

        A peninsula edge is an edge that intrudes into a face or hole without
        splitting it. These will always be safe to remove.

        0-----1
        |     |
        2--3  |
        |     |
        4-----5

        Here, edge 2--3 is a peninsula edge.
        """
        return edge.orig.valence == 1 or edge.dest.valence == 1

    def remove_vert(self, vert: Vert) -> Face:
        """Remove all edges around a vert.

        :param vert: vert to remove
        :returns: face or hole remaining
        :raise UnrecoverableManifoldMeshError: if a problem was found after we started
            altering the mesh (this SHOULD never happen).
        :raise ValueError: if vert is not in mesh
        :raise ValueError: if removing vert would create a non-manifold mesh

        How does this differ from consecutive calls to remove_edge?
            * checks (successfully as far as I can determine) that all edges are safe
              to remove before removing any.
            * orients remove_edge(orig, dest) calls so that holes fill hole-adjacent
              spaces rather than faces fill holes.
            * identifies and removes (one edge long) peninsula edges first

        Bridge edges are identified like so:
            * is orig valence > 1
            * is dest valence > 1
            * is edge.face == pair.face

        This simple test usually works; however, when removing multiple edges (around
        a vert) at one time, there are some special cases when a single bridge edge
        can be removed if all edges are removed in the correct order.

           0  1--2
           |  |  |
        3--4--5--6
           |
           7

        Here, edge 4--5 is a bridge edge. If it were removed by itself, it would
        create a disjoint face. However, we can safely remove all edges around vert
        4, maintaining a manifold mesh at every step, if they are removed in the
        correct order. The remaining face would be 5678, all contiguous.

        There are also cases of bridge verts, even where no bridge edges exist.

        0--1
        |  |
        2--3--4
           |  |
           5--6

        Here, there are no bridge edges, but removing vert 3 would create a disjoint
        mesh.

        Both of these cases are handled here.

        Passes attributes:
            * shared face attributes passed to new face
        """
        if vert.edge not in self.edges or vert.edge.orig != vert:
            msg = "vert is not in mesh. cannot remove"
            raise ValueError(msg)

        vert_edges = set(vert.edges)
        vert_faces = set(vert.all_faces)
        peninsulas = set(filter(self._is_peninsula, vert_edges))
        bridges = set(filter(self._is_bridge, vert_edges - peninsulas))

        if len(vert_edges - peninsulas) > len(vert_faces):
            msg = "removing vert would create non-manifold mesh"
            raise ValueError(msg)

        face: Face | None = None
        for edge in peninsulas:
            face = self.remove_edge(edge)
        for edge in vert_edges - peninsulas - bridges:
            face = self.remove_edge(edge)
        for edge in bridges:
            face = self.remove_edge(edge)

        if face is None:
            msg = "Failed to find face around vert. Vert has no edges."
            raise UnrecoverableManifoldMeshError(msg)
        return face

    def recursively_remove_peninsulas(self) -> None:
        r"""Remove all peninsula edges from the mesh.

        :raise UnrecoverableManifoldMeshError: if a problem was found after we started
            altering the mesh (this SHOULD never happen).

        This is only necessary if you are trying and failing to remove a face. A mesh
        face can end up as a polygon with tentacles at the corners. Some of these
        tentacles are made of bridge edges, but they will be safe to remove if the
        peninsula edges are removed first.

        0--1--2---3
              | 4 |
              |/  |
              5---6--7--8

        Here, edges 1-2 and 6-7 are bridge edges, but they will not be once
        peninsulas 0-1 and 7-8 are removed.
        """
        peninsulas = set(filter(self._is_peninsula, self.edges))
        if not peninsulas:
            return
        num_peninsulas = len(peninsulas)
        for edge in list(peninsulas):
            with suppress(ValueError):
                _ = self.remove_edge(edge)
                peninsulas.remove(edge)
        if len(peninsulas) == num_peninsulas:
            msg = "Failed to remove all peninsula edges"
            raise UnrecoverableManifoldMeshError(msg)

        self.recursively_remove_peninsulas()

    def remove_face(self, face: Face) -> Face:
        """Remove all edges around a face.

        :param face: face to remove
        :returns: face or hole remaining
        :raises: ValueError if the error was caught before any edges were removed
            (this SHOULD always be the case).
        :raise UnrecoverableManifoldMeshError: if a problem was found after we started
            altering the mesh (this SHOULD never happen).
        :raise ValueError: if face is not in mesh

        How does this differ from consecutive calls to remove_edge?
            * checks (successfully as far as I can determine) that all edges are safe
              to remove before removing any.

        Passes attributes:
            * shared face attributes passed to new face

        The test in this method should catch all cases where removing a face would
        break manifold, but it is a little too conservative. Repeated calls to
        remove_face have a tendancy to create "tentacles" of peninsula edges.

        0--1--2---3
              |   |
              |   |
              5---6--7--8

        This method will not remove face 5-6-3-2, because doing so would leave
        disjoint "tentacles" 0-1-2 and 6-7-8. It wouldn't be that difficult to
        identify these cases and surgically remove faces along with a minimum
        number of tentacles, but you'd have to somehow guess which tentacles to
        preserve, and all of this for no practical reason I can see. To remove a
        tentacled face, you may have to clean up the entire mesh by first running
        recursively_remove_peninsulas.
        """
        if face.edge not in self.edges:
            msg = "face is not in mesh"
            raise ValueError(msg)

        edges = set(face.edges)

        potential_bridges = {x for x in edges if x.orig.valence > 2}
        if len({x.pair.face for x in edges}) < len(potential_bridges):
            msg = par(
                """Removing this face would create a non-manifold mesh. One of this
                faces's edges is a bridge edge."""
            )
            raise ManifoldMeshError(msg)

        while edges:
            num_edges = len(edges)
            for edge in tuple(edges):
                with suppress(ValueError):
                    _ = self.remove_edge(edge)
                    edges.remove(edge)
            if len(edges) == num_edges:
                msg = "Failed to remove all edges around face"
                raise UnrecoverableManifoldMeshError(msg)
        return face

    def split_edge(self, edge: Edge) -> Vert:
        """Add a vert to the middle of an edge.

        :param edge: edge to be split
        :return: new vert in the middle of the edge
        :raise UnrecoverableManifoldMeshError: if a problem was found after we started
            altering the mesh (this SHOULD never happen).

        Passes attributes:
            * shared vert attributes passed to new vert
            * edge attributes passed to new edges
            * pair attributes passed to new pairs

        remove_edge will replace the original faces, so these are restored at the end
        of the method.
        """
        new_vert = self.new_vert().merge_from(*{edge.orig, edge.dest})
        edge_face = edge.face
        pair_face = edge.pair.face
        new_edge: Edge | None = None
        for orig, dest in ((edge.dest, new_vert), (new_vert, edge.orig)):
            new_edge = self.insert_edge(orig, dest, edge.face)
            _ = new_edge.split_from(edge.pair)
            _ = new_edge.pair.split_from(edge)
        if new_edge is None:
            msg = par(
                """new edge was not created. This is only possible if the mesh is
                broken. It didn't happen in this method, because nothing has been
                updated yet, but your mesh is definitely broken. I'll be suprised if
                you ever see this message."""
            )
            raise UnrecoverableManifoldMeshError(msg)
        _ = self.remove_edge(edge)
        _update_face_edges(edge_face, new_edge.pair)
        _update_face_edges(pair_face, new_edge)
        return new_vert

    def flip_edge(self, edge: Edge) -> Edge:
        """Flip an edge between two triangles.

        :param edge: Edge instance in self
        :return: None
        :raise ValueError: if edge is not in mesh

        * The edge must be between two triangles.
        * Only shared edge attributes will remain.
        * Only shared face attributes will remain.

        Warning: This can break your mesh if the quadrangle formed by the triangles
        on either side of the flipped edge is not convex. Not useful without some
        coordinate information to avoid this non-convex case.
        """
        pair = edge.pair
        if len(edge.face_edges) != 3 or len(pair.face_edges) != 3:
            msg = "can only flip an edge between two triangles"
            raise ValueError(msg)
        new_orig = edge.next.dest
        new_dest = pair.next.dest
        face = self.remove_edge(edge)
        return self.insert_edge(new_orig, new_dest, face)

    def _is_stitchable(self, edge: Edge) -> bool:
        r"""Return True if two edges be stitched (middle 2-side face removed).

        :param edge: edge which might be collapsed
        :return: True if the edge can be collapsed

        When collapsing an edge of a triangle, you end up with a slit face: a 2-sided
        face inside what would look like a single edge.

        0 ---------> 1 half edge 0; pair is half edge 1
        0 <--------- 1 half edge 1; pair is half edge 0
        0 ---------> 1 half edge 2; pair is half edge 3
        0 <--------- 1 half edge 3; pair is half edge 2

        Edge 01 (two half edges: half edge 0 and half edge 1) can be "stitched" to
        edge 23 to create

        0 ---------> 1 half edge 0; pair is half edge 3
        # half edge 1 is deleted
        # half edge 2 is deleted
        0 <--------- 1 half edge 3; pair is half edge 1

        If we didn't eliminate the slits, we might later try to collapse edge 01 and
        end up with an edge 23 that begins and ends at the same point. That could be
        handled as well, and maybe more simply, but the goal of this projects is to
        return a sane, intuitive mesh after every operation, and slit faces are not a
        part of that for me.

        So far, so good. But ...

        If the edge separates two triangles, you end up with 2 slit faces. These will
        also be stitched, and that can be the beginning of a problem.

           0
          /|\
         / 1 \
        / /|\ \
        |/ 2 \|
        / / \ \
        |/   \|
        3-----4

        This one will take a little imagination. You'll have to imagine that edges
        0-4, 0-3, 1-4, and 1-3 are straight. That leaves SIX (not five) faces:

        0-3-1, 0-1-4, 1-3-2, 1-2-4, 3-4-2, and the hole face around the entire
        figure: 4-3-0. This means edge 3-4 separates two triangles (3-4-2 and 4-3-0),
        both oriented counterclockwise.

        Collapse edge 3-4 and your six faces become (where * is the new point at the
        center of the collapsed edge):

        0-3-1 -> 0-*-1
        0-1-4 -> 0-1-*
        1-3-2 -> 1-*-2
        1-2-4 -> 1-2-*
        3-4-2 -> *-2 (internal triangle bordering original edge 3-4)
        4-3-0 -> *-0 (external triangle bordering original edge 3-4)

        New faces *-2 and *-0 will be "stitched" and deleted. That leaves four
        triangles. The problem with these four triangles is that edges 1-* and *-1
        each appear twice. We've followed all the rules and still ended up with a
        non-manifold mesh.

        If you have the spatial skills, you might be able to squint at that ascii art
        and find a solution, but that solution would require assumptions about
        geometry. These are easy assumptions to make in 2D, but they will require
        geometric information to confirm. This package only deals with connectivity,
        not geometry, so any such solution would be invalid.

        The solution I've chosen is this: if the stitching operation would break
        manifold, don't collapse a triangle. You will still be able to collapse any
        mesh into 0 faces, but you'll just need to be more careful (or try ...
        except) about the order in which you do it.

        This method identifies situations where stitching a collapsed triangle would
        break manifold.
        """
        pair = edge.pair
        tris = sum(x.face.sides == 3 for x in (edge, pair))
        orig_verts = set(edge.orig.neighbors)
        dest_verts = set(edge.dest.neighbors)
        return len(orig_verts & dest_verts) <= tris

    def collapse_edge(self, edge: Edge) -> Vert | None:
        r"""Collapse an Edge into a Vert.

        :param edge: Edge instance in self
        :return: Vert where edge used to be or None if this new vert does not exist
            in the mesh
        :raise ValueError: if edge is not in mesh
        :raise ValueError: if edge collapse would break manifold

        Warning: Some ugly things can happen here than can only be recognized and
        avoided by examining the geometry. This module only addresses connectivity,
        not geometry, but I've included this operation to experiment with and use
        carefully. Can flip faces and create linear faces.
        """
        if edge not in self.edges:
            msg = "edge is not in mesh"
            raise ValueError(msg)
        if not self._is_stitchable(edge):
            msg = "edge collapse would create non-manifold mesh"
            raise ValueError(msg)

        new_vert = self.new_vert().merge_from(*{edge.orig, edge.dest})
        for edge_ in set(edge.orig.edges) | set(edge.dest.edges):
            edge_.orig = new_vert

        adjacent_faces = sorted({edge.face, edge.pair.face}, key=lambda x: x.is_hole)

        self._point_away_from_edge(edge, edge.pair)
        edge.prev.next = edge.next
        edge.pair.prev.next = edge.pair.next
        self.edges -= {edge, edge.pair}

        # remove slits
        while adjacent_faces:
            face = adjacent_faces.pop(0)
            if len(self.edges) == 2:  # leave hole face unless explicitly collapsed
                break
            if face.edge not in self.edges:  # face has already been removed
                continue
            if len(face.edges) > 2:  # face still has volume. leave it
                continue
            # edge is a slit
            self._point_away_from_edge(*face.edges)
            face_edges = face.edges
            face_edges[0].pair.pair = face_edges[1].pair
            self.edges -= set(face_edges)

        # An edge collapses into a vert. In some cases, the vert will not exist in
        # the resulting mesh. There are cases where the vert *will* exist in the mesh
        # but be pointed to an edge that no longer exists. This catches those.
        if new_vert.edge in self.edges:
            return new_vert
        with suppress(StopIteration):
            new_vert.set_edge_without_side_effects(
                next(x for x in self.edges if x.orig is new_vert)
            )
            return new_vert
        return None

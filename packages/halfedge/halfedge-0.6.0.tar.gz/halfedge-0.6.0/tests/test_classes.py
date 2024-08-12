"""Test functions in classes.py.

created: 170204 14:22:23
"""

# pyright: reportPrivateUsage=false

from __future__ import annotations

import random
from typing import Any, Tuple, TypeVar

import pytest

from halfedge.half_edge_constructors import BlindHalfEdges
from halfedge.half_edge_elements import (
    Edge,
    Face,
    ManifoldMeshError,
    MeshElementBase,
    Vert,
    _function_lap,
)
from halfedge.half_edge_object import HalfEdges
from halfedge.half_edge_querries import StaticHalfEdges
from halfedge.type_attrib import (
    Attrib,
    ContagionAttrib,
    IncompatibleAttrib,
    NumericAttrib,
    StaticAttrib,
    Vector2Attrib,
    Vector3Attrib,
)
from tests.conftest import compare_circular_2, get_canonical_mesh

_TElemAttrib = TypeVar("_TElemAttrib", bound="Attrib[Any]")


class Flag(IncompatibleAttrib[int]):
    pass


class Score(NumericAttrib[float]):
    pass


# TODO: test that abstract classes cannot be instantiated


class MyAttrib(Attrib[int]):
    """An attribute with an integer value."""


class MyStaticAttrib(StaticAttrib[int]):
    """A static attribute with an integer value."""


class TestCannotInstantiateAbstractClasses:
    def test_cannot_instantiate_abstract_class(self) -> None:
        """Raise TypeError when instantiating an abstract class."""
        with pytest.raises(TypeError) as err:
            _: Attrib[Any] = Attrib()
        assert "cannot be instantiated" in err.value.args[0]

    def test_cannot_instantiate_contagion_attribute(self) -> None:
        """Raise TypeError when instantiating an abstract class."""
        with pytest.raises(TypeError) as err:
            _ = ContagionAttrib()
        assert "cannot be instantiated" in err.value.args[0]

    def test_cannot_instantiate_incompatible_attribute(self) -> None:
        """Raise TypeError when instantiating an abstract class."""
        with pytest.raises(TypeError) as err:
            _: IncompatibleAttrib[int] = IncompatibleAttrib()
        assert "cannot be instantiated" in err.value.args[0]

    def test_cannot_instantiate_numeric_attribute(self) -> None:
        """Raise TypeError when instantiating an abstract class."""
        with pytest.raises(TypeError) as err:
            _: NumericAttrib[int] = NumericAttrib()
        assert "cannot be instantiated" in err.value.args[0]

    def test_cannot_instantiate_vector_2_attribute(self) -> None:
        """Raise TypeError when instantiating an abstract class."""
        with pytest.raises(TypeError) as err:
            _ = Vector2Attrib()
        assert "cannot be instantiated" in err.value.args[0]

    def test_cannot_instantiate_vector_3_attribute(self) -> None:
        """Raise TypeError when instantiating an abstract class."""
        with pytest.raises(TypeError) as err:
            _ = Vector3Attrib()
        assert "cannot be instantiated" in err.value.args[0]

    def test_cannot_instantiate_static_attrib(self) -> None:
        """Raise TypeError when instantiating an abstract class."""
        with pytest.raises(TypeError) as err:
            _: StaticAttrib[Any] = StaticAttrib()
        assert "cannot be instantiated" in err.value.args[0]


class TestStaticAttrib:
    def test_attribute_error_if_no_value_set(self) -> None:
        """Raise AttributeError if no value set."""
        attrib = MyStaticAttrib()
        with pytest.raises(AttributeError):
            _ = attrib.value


class TestBlindHalfEdgesAttribSettersAndGetters:
    def test_set_attrib(self) -> None:
        """Set an attrib by passing a MeshElementBase instance"""
        mesh = BlindHalfEdges()
        attrib = MyStaticAttrib(7)
        mesh.set_attrib(attrib)
        stored_attrib = mesh.get_attrib(MyStaticAttrib)
        assert stored_attrib.value == 7
        assert stored_attrib.mesh is mesh


class TestAttribBaseClass:
    def test_attribute_error_if_no_value_set(self) -> None:
        """Raise AttributeError if no value set."""
        attrib = MyAttrib()
        with pytest.raises(AttributeError):
            _ = attrib.value

    def test_merge_returns_none(self) -> None:
        """Return None when attempting to merge MyAttrib instances."""
        attrib = MyAttrib()
        new_attrib = attrib.merge(None)
        assert new_attrib is None

    def test_split_returns_none(self) -> None:
        """Return None when attempting to split MyAttrib instances."""
        attrib = MyAttrib()
        new_attrib = attrib.split()
        assert new_attrib is None


class Contagion(ContagionAttrib):
    """A child blass of ContagionAttrib."""


class TestContagionAttrib:
    def test_return_on_merge_if_no_values(self) -> None:
        """Return None if no values are set."""
        attrib = Contagion()
        new_attrib = attrib.merge(None, None, None)
        assert new_attrib is None


class Incompatible(IncompatibleAttrib[int]):
    """A child class of IncompatibleAttrib."""


class TestIncompatibleAttrib:
    def test_return_self_on_split(self) -> None:
        """Return self when slicing from."""
        attrib = Incompatible()
        new_attrib = attrib.split()
        assert new_attrib is attrib


class Numeric(NumericAttrib[int]):
    """A child class of NumericAttrib."""


class TestNumericAttrib:
    def test_return_none_on_empty_merge(self) -> None:
        """Return None if no values are set."""
        attrib = Numeric()
        new_attrib = attrib.merge(None, None, None)
        assert new_attrib is None


class Vec2(Vector2Attrib):
    """A child class of Vector2Attrib."""


class TestVector2Attrib:

    def test_return_none_on_empty_merge(self) -> None:
        """Return None if no values are set."""
        attrib = Vec2()
        new_attrib = attrib.merge(None, None, None)
        assert new_attrib is None

    def test_average_xy_tuple_on_merge(self) -> None:
        """Return a new attribute with the average of all x and y values."""
        attribs = [Vec2((x, x)) for x in range(1, 6)]
        new_attrib = Vec2().merge(*attribs, None, None)
        assert new_attrib is not None
        assert new_attrib.value == (3, 3)

    def test_return_none_on_split(self) -> None:
        """Return None when attempting to split Vec2 instances."""
        attrib = Vec2()
        new_attrib = attrib.split()
        assert new_attrib is None

    def test_cannot_infer_value(self) -> None:
        """Raise AttributeError when attempting to infer a value."""
        attrib = Vec2()
        with pytest.raises(AttributeError) as err:
            _ = attrib._infer_value()
        assert "no provision for inferring a value" in err.value.args[0]


class Vec3(Vector3Attrib):
    """A child class of Vector3Attrib."""


class TestVector3Attrib:

    def test_return_none_on_empty_merge(self) -> None:
        """Return None if no values are set."""
        attrib = Vec3()
        new_attrib = attrib.merge(None, None, None)
        assert new_attrib is None

    def test_average_xy_tuple_on_merge(self) -> None:
        """Return a new attribute with the average of all x, y, and z values."""
        attribs = [Vec3((x, x, x)) for x in range(1, 6)]
        new_attrib = Vec3().merge(*attribs, None, None)
        assert new_attrib is not None
        assert new_attrib.value == (3, 3, 3)

    def test_return_none_on_split(self) -> None:
        """Return None when attempting to split Vec3 instances."""
        attrib = Vec3()
        new_attrib = attrib.split()
        assert new_attrib is None

    def test_cannot_infer_value(self) -> None:
        """Raise AttributeError when attempting to infer a value."""
        attrib = Vec3()
        with pytest.raises(AttributeError) as err:
            _ = attrib._infer_value()
        assert "no provision for inferring a value" in err.value.args[0]


class TestElemAttribs:
    def test_incompatible_merge_match(self) -> None:
        """Return a new attribute with same value if all values are equal"""
        attribs = [Incompatible(7, None) for _ in range(3)]
        new_attrib = Incompatible().merge(*attribs)
        assert new_attrib is not None
        assert new_attrib.value == 7

    def test_incompatible_merge_mismatch(self) -> None:
        """Return None if all values are not equal"""
        attribs = [Incompatible(7, None) for _ in range(3)]
        attribs.append(Incompatible(3))
        new_attrib = Incompatible().merge(*attribs)
        assert new_attrib is None

    def test_numeric_all_nos(self) -> None:
        """Return a new attribute with same value if all values are equal"""
        attribs = [Numeric(x) for x in range(1, 6)]
        new_attrib = Numeric().merge(*attribs)
        assert new_attrib is not None
        assert new_attrib.value == 3

    def test_lazy(self) -> None:
        """Given no value, LazyAttrib will try to infer a value from self.element"""

        class LazyAttrib(Attrib[int]):
            @classmethod
            def merge(cls, *merge_from: _TElemAttrib | None) -> _TElemAttrib | None:
                raise NotImplementedError()

            def _infer_value(self) -> int:
                return self.element.sn

        elem = MeshElementBase()
        elem.set_attrib(LazyAttrib())
        assert elem.get_attrib(LazyAttrib).value == elem.sn


class TestMeshElementBase:
    def test_lt_gt(self) -> None:
        """Sorts by sn."""
        elem1 = MeshElementBase()
        elem2 = MeshElementBase()
        assert (elem1 < elem2) == (elem1.sn < elem2.sn)
        assert (elem2 > elem1) == (elem2.sn > elem1.sn)

    def test_set_attrib(self) -> None:
        """Set an attrib by passing a MeshElementBase instance"""
        elem = MeshElementBase()
        elem_attrib = Flag(8)
        elem.set_attrib(elem_attrib)
        assert elem.get_attrib(Flag).value == 8

    def test_attribs_through_init(self) -> None:
        """MeshElement attributes are captured when passed to init"""
        base_with_attrib = MeshElementBase(Flag(7), Score(8))
        assert base_with_attrib.get_attrib(Flag).value == 7
        assert base_with_attrib.get_attrib(Score).value == 8

    def test_pointers_through_init(self) -> None:
        """Key, val pairs passed as kwargs fail if key does not have a setter"""
        with pytest.raises(TypeError):
            MeshElementBase(edge=MeshElementBase())  # type: ignore

    def test_fill_attrib(self) -> None:
        """Fill missing attrib values from fill_from"""
        elem1 = MeshElementBase(Score(8), Flag(3))
        elem2 = MeshElementBase(Score(6), Flag(3))
        elem3 = MeshElementBase(Flag(1))
        _ = elem3.merge_from(elem1, elem2)
        assert elem3.get_attrib(Flag).value == 1  # unchanged
        assert elem3.get_attrib(Score).value == 7  # filled


def test_edge_lap_succeeds(he_triangle: dict[str, Any]) -> None:
    """Returns to self when (func(func(func(....func(self))))) == self."""
    for edge in he_triangle["edges"]:
        assert _function_lap(lambda x: x.next, edge) == [
            edge,
            edge.next,
            edge.next.next,
        ]


def test_edge_lap_fails(he_triangle: dict[str, Any]) -> None:
    """Fails when self intersects."""
    edges = he_triangle["edges"]
    with pytest.raises(ManifoldMeshError) as err:
        _function_lap(lambda x: edges[1], edges[0])  # type: ignore
    assert "infinite" in err.value.args[0]


class Coordinate(IncompatibleAttrib[Tuple[int, int, int]]):
    """A subclass of IncompatibleAttrib."""

    pass


class TestInitVert:
    def setup_method(self) -> None:
        self.coordinate: Coordinate  # type: ignore
        self.edge: Edge  # type: ignore
        self.vert: Vert  # type: ignore
        self.coordinate = Coordinate((1, 2, 3))
        self.edge = Edge()
        self.vert = Vert(self.coordinate, edge=self.edge)

    def test_fill_from_preserves_pointers(self) -> None:
        """fill_from() will not overwrite pointers"""
        edge = Edge()
        vert = Vert(edge=edge)
        filler = Vert(edge=Edge())
        _ = vert.merge_from(filler)
        assert vert.edge is edge

    def test_coordinate_is_attribute(self) -> None:
        """Coordinate has been captured as an attribute"""
        result = self.vert.get_attrib(Coordinate).value
        expect = self.coordinate.value
        assert result == expect

    def test_coordinate_element_is_vert(self) -> None:
        """Coordinate.element is set during init/"""
        assert self.vert.get_attrib(Coordinate).element is self.vert

    def test_coordinate_value_has_not_changes(self) -> None:
        """Coordinate value is still (1, 2, 3)"""
        assert self.vert.get_attrib(Coordinate).value == (1, 2, 3)

    def test_points_to_edge(self) -> None:
        """vert.edge points to input edge"""
        assert self.vert.edge is self.edge

    def test_mirrored_assignment(self) -> None:
        """vert.edge assignment mirrored in edge.orig"""
        assert self.vert.edge.orig is self.vert


class TestInitEdge:

    def setup_method(self) -> None:
        self.coordinate: Coordinate  # type: ignore
        self.edge: Edge  # type: ignore
        self.orig: Vert  # type: ignore
        self.pair: Edge  # type: ignore
        self.face: Face  # type: ignore
        self.next: Edge  # type: ignore
        self.coordinate = Coordinate((1, 2, 3))
        self.edge = Edge()
        self.orig = Vert()
        self.pair = Edge()
        self.face = Face()
        self.next = Edge()
        self.edge = Edge(
            self.coordinate,
            orig=self.orig,
            pair=self.pair,
            face=self.face,
            next=self.next,
        )

    def test_coordinate_is_attribute(self) -> None:
        """Coordinate has been captured as an attribute"""
        assert self.edge.get_attrib(Coordinate).value == self.coordinate.value

    def test_coordinate_element_is_vert(self) -> None:
        """Coordinate.element is set during init/"""
        assert self.edge.get_attrib(Coordinate).element is self.edge

    def test_coordinate_value_has_not_changes(self) -> None:
        """Coordinate value is still (1, 2, 3)"""
        assert self.edge.get_attrib(Coordinate).value == (1, 2, 3)

    def test_points_to_orig(self) -> None:
        """vert.edge points to input edge"""
        assert self.edge.orig is self.orig

    def test_mirrored_orig(self) -> None:
        """edge.orig assignment mirrored in edge.orig"""
        assert self.edge.orig.edge is self.edge

    def test_points_to_pair(self) -> None:
        """vert.pair points to input edge"""
        assert self.edge.pair is self.pair

    def test_mirrored_pair(self) -> None:
        """edge.pair assignment mirrored in edge.pair"""
        assert self.edge.pair.pair is self.edge

    def test_points_to_face(self) -> None:
        """edge.face points to input face"""
        assert self.edge.face is self.face

    def test_mirrored_face(self) -> None:
        """edge.face assignment mirrored in edge.face"""
        assert self.edge.face.edge is self.edge

    def test_points_to_next(self) -> None:
        """edge.next points to input edge"""
        assert self.edge.next is self.next


class TestInitFace:

    def setup_method(self) -> None:
        self.coordinate: Coordinate  # type: ignore
        self.edge: Edge  # type: ignore
        self.face: Face  # type: ignore
        self.coordinate = Coordinate((1, 2, 3))
        self.edge = Edge()
        self.face = Face(self.coordinate, edge=self.edge)

    def test_coordinate_is_attribute(self) -> None:
        """Coordinate has been captured as an attribute"""
        assert self.face.get_attrib(Coordinate).value is self.coordinate.value

    def test_coordinate_element_is_vert(self) -> None:
        """Coordinate.element is set during init/"""
        assert self.face.get_attrib(Coordinate).element is self.face

    def test_coordinate_value_has_not_changes(self) -> None:
        """Coordinate value is still (1, 2, 3)"""
        assert self.face.get_attrib(Coordinate).value == (1, 2, 3)

    def test_points_to_edge(self) -> None:
        """face.edge points to input edge"""
        assert self.face.edge is self.edge

    def test_mirrored_orig(self) -> None:
        """face.edge assignment mirrored in face.edge"""
        assert self.face.edge.face is self.face


class TestElementSubclasses:
    """Test all three _MeshElementBase children."""

    def test_edge_face_edges(self, he_triangle: dict[str, Any]) -> None:
        """Edge next around face."""
        for edge in he_triangle["edges"]:
            assert tuple(edge.face_edges) == (edge, edge.next, edge.next.next)

    def test_face_edges(self, he_triangle: dict[str, Any]) -> None:
        """Finds all edges, starting at face.edge."""
        for face in he_triangle["faces"]:
            assert tuple(face.edges) == tuple(face.edge.face_edges)

    def test_edge_face_verts(self, he_triangle: dict[str, Any]) -> None:
        """Is equivalent to edge.pair.next around orig."""
        for edge in he_triangle["edges"]:
            assert tuple(edge.vert_edges) == (edge, edge.pair.next)

    def test_vert_edge(self) -> None:
        """Find vert edge in mesh"""
        vert = Vert()
        edge = Edge(orig=vert)
        _ = StaticHalfEdges({edge})
        assert vert.edge == edge

    def test_vert_edges(self, he_triangle: dict[str, Any]) -> None:
        """Is equivalent to vert_edges for vert.edge."""
        for vert in he_triangle["verts"]:
            assert tuple(vert.edges) == tuple(vert.edge.vert_edges)

    def test_vert_verts(self, he_triangle: dict[str, Any]) -> None:
        """Is equivalent to vert_edge.dest for vert.edge."""
        for vert in he_triangle["verts"]:
            assert vert.neighbors == [x.dest for x in vert.edge.vert_edges]

    def test_vert_valence(self, he_triangle: dict[str, Any]) -> None:
        """Valence is two for every corner in a triangle."""
        for vert in he_triangle["verts"]:
            assert vert.valence == 2

    def test_prev_by_face_edges(self, he_triangle: dict[str, Any]) -> None:
        """Previous edge will 'next' to self."""
        for edge in he_triangle["edges"]:
            assert edge.prev.next == edge

    @staticmethod
    def test_dest_is_next_orig(he_triangle: dict[str, Any]) -> None:
        """Finds orig of next or pair edge."""
        for edge in he_triangle["edges"]:
            assert edge.dest is edge.next.orig

    @staticmethod
    def test_dest_is_pair_orig(he_triangle: dict[str, Any]) -> None:
        """Returns pair orig if next.orig fails."""
        edge = random.choice(he_triangle["edges"])
        edge.next = None
        assert edge.dest is edge.pair.orig

    @staticmethod
    def test_face_verts(he_triangle: dict[str, Any]) -> None:
        """Returns orig for every edge in face_verts."""
        for face in he_triangle["faces"]:
            assert tuple(face.verts) == tuple(face.edge.face_verts)


def test_half_edges_init(he_triangle: dict[str, Any]) -> None:
    """Verts, edges, faces, and holes match hand-calculated coordinates."""
    verts = set(he_triangle["verts"])
    edges = set(he_triangle["edges"])
    faces = set(he_triangle["faces"])
    holes = set(he_triangle["holes"])

    mesh = StaticHalfEdges(edges)

    assert mesh.verts == verts
    assert mesh.edges == edges
    assert mesh.faces == faces
    assert mesh.holes == holes


class TestHalfEdges:
    """Keep the linter happy."""

    def test_vl(
        self, meshes_vlvi: dict[str, Any], he_cube: HalfEdges, he_grid: HalfEdges
    ) -> None:
        """Converts unaltered mesh verts back to input vl."""
        assert {x.get_attrib(Coordinate).value for x in he_cube.vl} == set(
            meshes_vlvi["cube_vl"]
        )
        assert {x.get_attrib(Coordinate).value for x in he_grid.vl} == set(
            meshes_vlvi["grid_vl"]
        )

    def test_vi(
        self, meshes_vlvi: dict[str, Any], he_cube: HalfEdges, he_grid: HalfEdges
    ) -> None:
        """Convert unaltered mesh faces back to input vi.
        Demonstrates preservation of face edge beginning point."""
        _ = compare_circular_2(he_cube.fi, meshes_vlvi["cube_vi"])
        _ = compare_circular_2(he_grid.fi, meshes_vlvi["grid_vi"])

    def test_hi(self, meshes_vlvi: dict[str, Any], he_grid: HalfEdges) -> None:
        """Convert unaltered mesh holes back to input holes."""
        expect = get_canonical_mesh(meshes_vlvi["grid_vl"], meshes_vlvi["grid_hi"])
        result = get_canonical_mesh(
            [x.get_attrib(Coordinate).value for x in he_grid.vl], he_grid.hi
        )
        assert expect == result


def test_half_edges_boundary_edges(he_grid: HalfEdges) -> None:
    """12 edges on grid. All face holes."""
    edges = he_grid.boundary_edges
    assert len(edges) == 12
    assert all(x.face.is_hole for x in edges)


def test_half_edges_boundary_verts(he_grid: HalfEdges) -> None:
    """12 verts on grid. All valence 2 or 3."""
    verts = he_grid.boundary_verts
    assert len(verts) == 12
    assert all(x.valence in (2, 3) for x in verts)


def test_half_edges_interior_edges(he_grid: HalfEdges) -> None:
    """36 in grid. All face Faces."""
    edges = he_grid.interior_edges
    assert len(edges) == 36
    assert not any(x.face.is_hole for x in edges)


def test_half_edges_interior_verts(he_grid: HalfEdges) -> None:
    """4 in grid. All valence 4"""
    verts = he_grid.interior_verts
    assert len(verts) == 4
    assert all(x.valence == 4 for x in verts)

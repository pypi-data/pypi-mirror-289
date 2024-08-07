from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict
from xml.etree.ElementTree import Element, SubElement, tostring


@dataclass
class Geometry:
    coordinates: List
    name: str
    color_hex: str
    metadata: Dict[str, List[str]] = field(default_factory=lambda: defaultdict(list))

    @property
    def geometry_type(self):
        raise NotImplementedError("Subclasses should implement this property")

    @property
    def sidc(self):
        raise NotImplementedError("Subclasses should implement this property")

    def to_feature(self):
        return {
            "type": "Feature",
            "properties": {
                "name": self.name,
                "sidc": self.sidc,
                "outline-color": self.color_hex,
                "comments": []
            },
            "geometry": {
                "type": self.geometry_type,
                "coordinates": self.coordinates
            }
        }

    def to_placemark(self):
        placemark = Element("Placemark")
        name = SubElement(placemark, "name")
        name.text = self.name
        style = SubElement(placemark, "Style")
        line_style = SubElement(style, "LineStyle")
        color = SubElement(line_style, "color")
        color.text = self.color_hex

        if self.geometry_type == "Point":
            geometry_element = SubElement(placemark, "Point")
            coordinates = SubElement(geometry_element, "coordinates")
            coordinates.text = f"{self.coordinates[0]},{self.coordinates[1]}"

        elif self.geometry_type == "LineString":
            geometry_element = SubElement(placemark, "LineString")
            coordinates = SubElement(geometry_element, "coordinates")
            coordinates.text = " ".join([f"{coord[0]},{coord[1]}" for coord in self.coordinates])

        elif self.geometry_type == "Polygon":
            geometry_element = SubElement(placemark, "Polygon")
            outer_boundary_is = SubElement(geometry_element, "outerBoundaryIs")
            linear_ring = SubElement(outer_boundary_is, "LinearRing")
            coordinates = SubElement(linear_ring, "coordinates")
            coordinates.text = " ".join([f"{coord[0]},{coord[1]}" for ring in self.coordinates for coord in ring])

        return tostring(placemark)


@dataclass
class Point(Geometry):
    coordinates: List[float]

    @property
    def geometry_type(self):
        return "Point"

    @property
    def sidc(self):
        return "10012500001313000000"


@dataclass
class Line(Geometry):
    coordinates: List[List[float]]

    @property
    def geometry_type(self):
        return "LineString"

    @property
    def sidc(self):
        return "10016600001100000000"


@dataclass
class Polygon(Geometry):
    coordinates: List[List[List[float]]]

    @property
    def geometry_type(self):
        return "Polygon"

    @property
    def sidc(self):
        return "10012500001505010000"

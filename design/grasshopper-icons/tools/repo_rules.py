"""Repository-specific classification decisions for SAM_Topologic (the only non-shared tool file).

OVERRIDES     : component display name -> (object glyph, op, extra)   extra: None | "plural" | "library" | note
PARAM_OBJECTS : param type key (Goo<X>Param class or typeof(X) name) -> glyph | (glyph, container, plural)
OBJECTS/VERBS : extra noun/verb rules tried before the shared ones (same shapes as SAM's OBJECTS/VERBS)
"""
OVERRIDES = {
    # Topologic <-> SAM: import/export on the SAM object; Rhino <-> Topologic = convert; topology itself = ext `cellComplex`
    "CellComplex.ByCells": ("cellComplex", "create", None), "Topology.FacesCellComplex": ("cellComplex", "create", None),
    "CellComplex.Faces": ("face", "get", "plural"),
    "SAMAnalytical.Topology": ("object", "export", None), "SAMGeometry.Topology": ("geometry", "export", None),
    "Topology.SAMGeometry": ("geometry", "import", None), "Geometry.Topology": ("cellComplex", "convert", "Rhino -> Topologic"),
    "Topology.Geometry": ("geometry", "convert", "Topologic -> Rhino"), "Topology.CreateCluster": ("cellComplex", "create", "plural"),
    "Topology.Adjacencies": ("cluster", "get", "adjacency list"), "Topology.Analyze": ("cellComplex", "analyse", None),
    "Topology.CellContains": ("cellComplex", "validate", None), "Topology.CenterOfMass": ("points", "calculate", None),
    "Topology.Centroid": ("points", "get", None), "Topology.Inspect": ("cellComplex", "inspect", None),
    "Topology.Slice": ("cellComplex", "split", None), "Topology.Triangulate": ("face", "triangulate", None),
    "SAMShells.Split": ("shell", "split", None),
}
PARAM_OBJECTS = {}
OBJECTS = []
VERBS = []

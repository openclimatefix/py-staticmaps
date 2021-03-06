#!/usr/bin/env python

# py-staticmaps
# Copyright (c) 2020 Florian Pigorsch; see /LICENSE for licensing information

import staticmaps

context = staticmaps.Context()
context.set_tile_provider(staticmaps.tile_provider_OSM)

freiburg_polygon = [
    (47.96881, 7.79045),
    (47.96866, 7.78610),
    (47.97134, 7.77874),
    (47.97305, 7.77517),
    (47.97464, 7.77492),
    (47.97631, 7.77099),
    (47.97746, 7.77029),
    (47.97840, 7.76794),
    (47.97700, 7.76551),
    (47.97683, 7.76318),
    (47.97852, 7.75531),
    (47.97940, 7.75589),
    (47.97791, 7.74972),
    (47.97764, 7.74706),
    (47.97817, 7.74235),
    (47.97844, 7.73899),
    (47.97696, 7.73655),
    (47.97688, 7.73311),
    (47.97549, 7.73054),
    (47.97563, 7.73048),
    (47.97575, 7.73039),
    (47.97585, 7.73029),
    (47.97596, 7.73016),
    (47.97606, 7.73000),
    (47.97626, 7.72969),
    (47.97653, 7.72913),
    (47.97697, 7.72815),
    (47.97741, 7.72731),
    (47.97766, 7.72677),
    (47.97781, 7.72642),
    (47.97588, 7.72338),
    (47.97530, 7.72410),
    (47.97337, 7.72093),
    (47.97084, 7.72396),
    (47.96778, 7.71903),
    (47.96279, 7.70870),
    (47.95923, 7.70065),
    (47.95921, 7.70010),
    (47.95930, 7.69948),
    (47.95943, 7.69903),
    (47.95972, 7.69828),
    (47.96011, 7.69759),
    (47.96057, 7.69705),
    (47.96120, 7.69628),
    (47.96173, 7.69550),
    (47.96212, 7.69469),
    (47.96246, 7.69364),
    (47.96291, 7.69218),
    (47.96324, 7.69083),
    (47.96336, 7.68970),
    (47.96339, 7.68916),
    (47.96336, 7.68863),
    (47.96323, 7.68810),
    (47.96298, 7.68821),
    (47.96125, 7.68781),
    (47.96241, 7.68398),
    (47.96057, 7.67924),
    (47.95939, 7.67770),
    (47.96083, 7.67572),
    (47.96408, 7.67154),
    (47.96421, 7.66967),
    (47.96260, 7.66806),
    (47.96508, 7.66479),
    (47.96557, 7.66246),
    (47.96650, 7.66314),
    (47.97034, 7.66592),
    (47.97291, 7.66665),
    (47.97433, 7.67031),
    (47.97454, 7.67594),
    (47.97609, 7.67900),
    (47.97857, 7.67843),
    (47.98179, 7.68004),
    (47.98349, 7.68058),
    (47.98331, 7.68246),
    (47.98606, 7.68325),
    (47.98911, 7.68388),
    (47.98991, 7.68081),
    (47.99061, 7.68118),
    (47.99158, 7.67885),
    (47.99274, 7.67947),
    (47.99404, 7.67805),
    (47.99583, 7.67903),
    (47.99684, 7.67958),
    (48.00043, 7.68554),
    (48.00340, 7.69160),
    (48.00585, 7.69506),
    (48.00859, 7.70018),
    (48.01007, 7.70648),
    (48.01238, 7.70833),
    (48.01281, 7.70504),
    (48.01410, 7.70576),
    (48.01627, 7.70602),
    (48.01674, 7.70434),
    (48.01869, 7.70359),
    (48.02023, 7.70452),
    (48.02153, 7.70300),
    (48.02313, 7.70393),
    (48.02343, 7.70323),
    (48.02467, 7.70376),
    (48.02598, 7.70348),
    (48.02608, 7.70183),
    (48.02781, 7.70221),
    (48.02867, 7.70376),
    (48.03147, 7.70512),
    (48.03325, 7.70672),
    (48.03527, 7.70826),
    (48.03415, 7.71157),
    (48.03383, 7.71384),
    (48.03303, 7.71367),
    (48.03347, 7.71659),
    (48.03442, 7.71670),
    (48.03468, 7.71945),
    (48.03391, 7.72156),
    (48.03425, 7.72344),
    (48.03515, 7.72399),
    (48.03508, 7.72531),
    (48.03531, 7.72853),
    (48.03835, 7.73153),
    (48.03804, 7.73211),
    (48.03655, 7.73446),
    (48.03300, 7.73353),
    (48.03107, 7.73673),
    (48.02993, 7.73999),
    (48.02882, 7.74051),
    (48.02674, 7.74396),
    (48.02632, 7.74637),
    (48.02538, 7.74663),
    (48.02276, 7.75155),
    (48.02133, 7.75100),
    (48.01890, 7.75728),
    (48.01859, 7.75816),
    (48.02012, 7.75889),
    (48.02221, 7.75889),
    (48.02092, 7.76242),
    (48.02049, 7.76223),
    (48.01943, 7.76461),
    (48.01928, 7.76621),
    (48.01856, 7.76749),
    (48.01794, 7.76782),
    (48.01752, 7.76889),
    (48.01470, 7.76774),
    (48.02290, 7.77924),
    (48.02566, 7.77755),
    (48.02719, 7.77952),
    (48.02645, 7.78374),
    (48.02857, 7.78927),
    (48.03012, 7.78820),
    (48.03288, 7.78634),
    (48.03379, 7.78850),
    (48.03666, 7.79030),
    (48.04103, 7.79139),
    (48.04240, 7.79077),
    (48.04386, 7.79240),
    (48.04531, 7.79296),
    (48.05310, 7.79636),
    (48.05344, 7.79289),
    (48.05528, 7.79529),
    (48.05906, 7.79708),
    (48.05911, 7.79559),
    (48.06106, 7.79606),
    (48.06116, 7.80123),
    (48.06112, 7.80387),
    (48.06187, 7.80571),
    (48.06248, 7.80614),
    (48.06389, 7.80521),
    (48.07111, 7.81502),
    (48.06953, 7.81751),
    (48.07021, 7.82013),
    (48.07003, 7.82195),
    (48.06903, 7.82471),
    (48.06797, 7.82523),
    (48.06656, 7.82650),
    (48.06540, 7.82765),
    (48.06197, 7.83217),
    (48.06142, 7.83274),
    (48.06055, 7.83347),
    (48.05957, 7.83399),
    (48.05857, 7.83469),
    (48.05600, 7.83857),
    (48.05565, 7.83957),
    (48.05406, 7.84395),
    (48.05385, 7.84448),
    (48.05354, 7.84540),
    (48.05341, 7.84582),
    (48.05318, 7.84656),
    (48.05291, 7.84751),
    (48.05231, 7.84965),
    (48.05204, 7.85060),
    (48.05108, 7.85095),
    (48.04891, 7.85175),
    (48.04795, 7.85210),
    (48.04686, 7.85245),
    (48.04589, 7.85272),
    (48.04506, 7.85291),
    (48.04406, 7.85308),
    (48.04306, 7.85322),
    (48.04062, 7.85350),
    (48.03991, 7.85360),
    (48.03922, 7.85372),
    (48.03840, 7.85390),
    (48.03774, 7.85408),
    (48.03709, 7.85432),
    (48.03689, 7.85439),
    (48.03671, 7.85447),
    (48.03659, 7.85454),
    (48.03640, 7.85477),
    (48.03460, 7.85836),
    (48.03507, 7.86373),
    (48.03414, 7.86673),
    (48.03064, 7.87091),
    (48.02987, 7.87069),
    (48.02946, 7.87253),
    (48.03145, 7.87524),
    (48.02806, 7.87812),
    (48.02685, 7.87847),
    (48.02505, 7.88080),
    (48.02301, 7.88182),
    (48.02215, 7.88373),
    (48.02283, 7.88523),
    (48.01932, 7.89069),
    (48.01914, 7.89351),
    (48.01586, 7.89826),
    (48.01527, 7.89734),
    (48.01673, 7.89289),
    (48.01635, 7.88893),
    (48.02102, 7.88394),
    (48.01896, 7.87925),
    (48.01926, 7.87875),
    (48.01953, 7.87825),
    (48.01996, 7.87741),
    (48.02019, 7.87690),
    (48.02034, 7.87654),
    (48.02061, 7.87585),
    (48.02068, 7.87566),
    (48.02079, 7.87529),
    (48.01961, 7.87299),
    (48.01678, 7.87206),
    (48.01368, 7.87752),
    (48.01155, 7.88520),
    (48.01015, 7.88816),
    (48.01025, 7.90032),
    (48.01205, 7.90414),
    (48.01328, 7.90722),
    (48.01186, 7.91342),
    (48.01558, 7.92057),
    (48.01525, 7.92178),
    (48.01401, 7.92648),
    (48.01397, 7.92664),
    (48.00607, 7.92835),
    (48.00344, 7.92822),
    (48.00087, 7.92718),
    (47.99595, 7.92991),
    (47.99085, 7.93031),
    (47.98881, 7.92967),
    (47.98933, 7.92781),
    (47.98751, 7.92625),
    (47.98607, 7.92768),
    (47.98531, 7.92483),
    (47.98072, 7.92489),
    (47.98072, 7.92476),
    (47.98071, 7.92455),
    (47.98069, 7.92433),
    (47.98056, 7.92348),
    (47.98042, 7.92224),
    (47.98010, 7.92000),
    (47.97992, 7.91856),
    (47.97984, 7.91792),
    (47.97980, 7.91783),
    (47.97946, 7.91582),
    (47.97938, 7.91520),
    (47.97934, 7.91479),
    (47.97930, 7.91437),
    (47.97928, 7.91397),
    (47.97929, 7.91360),
    (47.97811, 7.91462),
    (47.97787, 7.91485),
    (47.97765, 7.91507),
    (47.97742, 7.91533),
    (47.97721, 7.91561),
    (47.97661, 7.91655),
    (47.97641, 7.91685),
    (47.97631, 7.91698),
    (47.97619, 7.91709),
    (47.97608, 7.91721),
    (47.97596, 7.91729),
    (47.97570, 7.91745),
    (47.97556, 7.91753),
    (47.97526, 7.91766),
    (47.97510, 7.91771),
    (47.97480, 7.91778),
    (47.97465, 7.91780),
    (47.97453, 7.91817),
    (47.97424, 7.91915),
    (47.97412, 7.91953),
    (47.97399, 7.91989),
    (47.97392, 7.92008),
    (47.97384, 7.92024),
    (47.97375, 7.92040),
    (47.97366, 7.92053),
    (47.97355, 7.92067),
    (47.97333, 7.92091),
    (47.97308, 7.92113),
    (47.97246, 7.92160),
    (47.97220, 7.92182),
    (47.97197, 7.92204),
    (47.97174, 7.92231),
    (47.97144, 7.92273),
    (47.97106, 7.92332),
    (47.97057, 7.92412),
    (47.96968, 7.92270),
    (47.96751, 7.92175),
    (47.96746, 7.91814),
    (47.96484, 7.91532),
    (47.96283, 7.91509),
    (47.95817, 7.91742),
    (47.95709, 7.91868),
    (47.95522, 7.91937),
    (47.95314, 7.92086),
    (47.95094, 7.92471),
    (47.94997, 7.92434),
    (47.94623, 7.92482),
    (47.94349, 7.92455),
    (47.94159, 7.92406),
    (47.93999, 7.92473),
    (47.93738, 7.92204),
    (47.93578, 7.92008),
    (47.93465, 7.91698),
    (47.93008, 7.91304),
    (47.92912, 7.90950),
    (47.92778, 7.90751),
    (47.92457, 7.90663),
    (47.91760, 7.90998),
    (47.91444, 7.90916),
    (47.91374, 7.90520),
    (47.91198, 7.90137),
    (47.91216, 7.89916),
    (47.91048, 7.89628),
    (47.91013, 7.89369),
    (47.90662, 7.89295),
    (47.90421, 7.88497),
    (47.90426, 7.88285),
    (47.90411, 7.88047),
    (47.90339, 7.87350),
    (47.90419, 7.87058),
    (47.90827, 7.86947),
    (47.90928, 7.86828),
    (47.91253, 7.86548),
    (47.91300, 7.86290),
    (47.91537, 7.86246),
    (47.91644, 7.86409),
    (47.91694, 7.86343),
    (47.91759, 7.86292),
    (47.91827, 7.86259),
    (47.91906, 7.86235),
    (47.91996, 7.86219),
    (47.92077, 7.86215),
    (47.92157, 7.86222),
    (47.92242, 7.86230),
    (47.92326, 7.86239),
    (47.92360, 7.86241),
    (47.92342, 7.86750),
    (47.92368, 7.86687),
    (47.92392, 7.86637),
    (47.92410, 7.86605),
    (47.92437, 7.86561),
    (47.92458, 7.86535),
    (47.92481, 7.86509),
    (47.92505, 7.86487),
    (47.92531, 7.86466),
    (47.92545, 7.86458),
    (47.92571, 7.86442),
    (47.92599, 7.86428),
    (47.92627, 7.86417),
    (47.92656, 7.86409),
    (47.92695, 7.86403),
    (47.92722, 7.86401),
    (47.92764, 7.86403),
    (47.92792, 7.86406),
    (47.92834, 7.86413),
    (47.92871, 7.86422),
    (47.92874, 7.86700),
    (47.93240, 7.86742),
    (47.93406, 7.86919),
    (47.93100, 7.87444),
    (47.93480, 7.87711),
    (47.94120, 7.87677),
    (47.94350, 7.87871),
    (47.94859, 7.87902),
    (47.94921, 7.87558),
    (47.95148, 7.87101),
    (47.95115, 7.86835),
    (47.94939, 7.87002),
    (47.94951, 7.86193),
    (47.94883, 7.85817),
    (47.95021, 7.85558),
    (47.95214, 7.85401),
    (47.95530, 7.85329),
    (47.95673, 7.84896),
    (47.96079, 7.84887),
    (47.96227, 7.84587),
    (47.96352, 7.84337),
    (47.96320, 7.84009),
    (47.96505, 7.83786),
    (47.96602, 7.83423),
    (47.96973, 7.83683),
    (47.97127, 7.83730),
    (47.97264, 7.83662),
    (47.97247, 7.83296),
    (47.97240, 7.82634),
    (47.97242, 7.82278),
    (47.97116, 7.82100),
    (47.97054, 7.82011),
    (47.97021, 7.81859),
    (47.96796, 7.81701),
    (47.96768, 7.81300),
    (47.96724, 7.81219),
    (47.96592, 7.80894),
    (47.96425, 7.80478),
    (47.96369, 7.80338),
    (47.96430, 7.80115),
    (47.96484, 7.79920),
    (47.96712, 7.79471),
    (47.96883, 7.79090),
    (47.96881, 7.79045),
]

context.add_object(
    staticmaps.Area(
        [staticmaps.create_latlng(lat, lng) for lat, lng in freiburg_polygon],
        fill_color=staticmaps.parse_color("#00FF003F"),
        width=2,
        color=staticmaps.BLUE,
    )
)

# render png
if staticmaps.cairo_is_supported():
    image = context.render_cairo(800, 500)
    image.write_to_png("freiburg_area.png")

# render svg
svg_image = context.render_svg(800, 500)
with open("freiburg_area.svg", "w", encoding="utf-8") as f:
    svg_image.write(f, pretty=True)

# -*- coding: utf-8 -*-
"""
بناء مجسم ثلاثي الأبعاد (GLB) لأرض مقسمة بين الورثة - المطري كونسلت
أرض 100م (شرق-غرب) × 30م (شمال-جنوب)
التفريض: زوجة 1/8 ، الباقي للعصبة (ولدان وبنت) للذكر مثل حظ الأنثيين
زوجة = 1/8 = 12.5%  → 12.5م
ولد  = 7/40 ×2... نحسب: الباقي 7/8 على 5 أسهم → ولد 2/5×7/8=7/20=35% ، بنت 7/40=17.5%
"""
import numpy as np
import trimesh
from trimesh.creation import extrude_polygon
from shapely.geometry import Polygon

L, W = 100.0, 30.0  # طول × عرض بالمتر

# الأنصبة (نسبة من المساحة) والتقسيم شرائح عمودية من الشرق إلى الغرب
heirs = [
    ("الزوجة",  0.125, (26, 82, 118)),    # أزرق المطري #1a5276
    ("الابن الأول", 0.35, (192, 57, 43)), # أحمر #c0392b
    ("الابن الثاني", 0.35, (40, 116, 80)),# أخضر
    ("البنت",   0.175, (202, 138, 4)),    # ذهبي
]

scene = trimesh.Scene()
x0 = 0.0
slab_h = 0.6  # سماكة القطعة بالمتر (مبالغ فيها قليلاً للوضوح في AR)

for name, share, rgb in heirs:
    seg = L * share
    poly = Polygon([(x0, 0), (x0 + seg, 0), (x0 + seg, W), (x0, W)])
    mesh = extrude_polygon(poly, slab_h)
    mesh.visual.face_colors = [*rgb, 255]
    scene.add_geometry(mesh, node_name=name)
    x0 += seg

# خطوط فاصلة بين القطع (جدران رفيعة بيضاء)
x0 = 0.0
for name, share, _ in heirs[:-1]:
    x0 += L * share
    wall = trimesh.creation.box(extents=[0.25, W, slab_h + 0.5])
    wall.apply_translation([x0, W / 2, (slab_h + 0.5) / 2])
    wall.visual.face_colors = [255, 255, 255, 255]
    scene.add_geometry(wall)

# سور خارجي رفيع داكن
def border(extents, pos):
    b = trimesh.creation.box(extents=extents)
    b.apply_translation(pos)
    b.visual.face_colors = [30, 41, 59, 255]
    scene.add_geometry(b)

bh = slab_h + 1.0
border([L + 0.4, 0.2, bh], [L/2, -0.1, bh/2])
border([L + 0.4, 0.2, bh], [L/2, W + 0.1, bh/2])
border([0.2, W, bh], [-0.1, W/2, bh/2])
border([0.2, W, bh], [L + 0.1, W/2, bh/2])

# توسيط المجسم وتدويره ليكون مستوياً (Y-up في glTF)
scene.apply_translation([-L/2, -W/2, 0])
scene.apply_transform(trimesh.transformations.rotation_matrix(-np.pi/2, [1, 0, 0]))

# تصغير 1:100 ليظهر بحجم طاولة في AR (1م حقيقي = 1سم)
scene.apply_scale(0.01)

scene.export("/home/claude/ar-croquis/parcel.glb")
print("GLB OK -", round(sum(s for _, s, _ in heirs), 4))
for n, s, _ in heirs:
    print(f"{n}: {s*100}% = {L*W*s:.1f} م²  (عرض الشريحة {L*s:.2f} م)")

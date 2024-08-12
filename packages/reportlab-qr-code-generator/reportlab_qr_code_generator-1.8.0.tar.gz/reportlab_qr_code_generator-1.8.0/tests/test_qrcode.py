# -*- coding: utf-8 -*-
import array
import math
from copy import deepcopy

import pytest
from reportlab.lib.units import toLength
from reportlab.pdfgen import canvas

from reportlab_qr_code import qr, qr_draw, reportlab_image_factory, build_qrcode, parse_params_string, ReportlabImageBase


def get_canvas():
	return canvas.Canvas("hello.pdf")


def test_simple():
	c = get_canvas()
	qr(c, ';text;Text')


def test_wrong_format():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Wrong format, .*"):
		qr(c, ';')

def test_wrong_params_format():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Wrong format of parameters .*"):
		qr(c, 'xx;text;Text')


def test_wrong_params():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Unknown attribute .*"):
		qr(c, 'xx=yy;text;Text')


def test_unknown_format():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Unknown format .*"):
		qr(c, ';wrong;Text')


def test_wrong_type():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Wrong value .*"):
		qr(c, 'radius=z;text;Text')


def test_base64():
	c = get_canvas()
	qr(c, ';base64;QmFzZSA2NCBlbmNvZGVk')


def test_wrong_base64_padding():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Wrong base64 .*"):
		qr(c, ';base64;ze')


def test_custom_size():
	qr(get_canvas(), 'size=3cm;text;Custom size') # check generator errors
	img = build_qrcode(*parse_params_string('size=3cm;text;Custom size'))
	assert img.size == toLength("3cm")


def test_custom_colors():
	c = get_canvas()
	qr(c, 'bg=#eeeeee,fg=#a00000;text;Custom colors')


def test_custom_percentage_padding():
	qr(get_canvas(), 'padding=20%;text;Padding 20%')
	img = build_qrcode(*parse_params_string('size=100,padding=20%;text;Padding 20%'))
	assert img.padding == 20.


def test_custom_absolute_padding():
	qr(get_canvas(), 'padding=1cm;text;Padding 1cm')
	img = build_qrcode(*parse_params_string('padding=1cm;text;Padding 1cm'))
	assert img.padding == pytest.approx(toLength('1cm'), 0.01)


def test_custom_pixel_padding():
	qr(get_canvas(), 'padding=1;text;Padding 1 pixel')
	img = build_qrcode(*parse_params_string('padding=1;text;Padding 1 pixel'))
	padding_size = img.padding
	pixel_size = img.size / (img.width + 2.0)
	assert padding_size == pytest.approx(pixel_size, 0.01)


def test_radius():
	qr(get_canvas(), 'radius=0.5;text;Radius')
	img = build_qrcode(*parse_params_string('radius=0.5;text;Radius'))
	assert img.radius == 0.5
	assert img.enhanced_path == False


def test_default_enhanced_path():
	img = build_qrcode(*parse_params_string(';text;Default enhanced'))
	assert img.enhanced_path == True


def test_override_enhanced():
	qr(get_canvas(), 'radius=0.5,enhanced_path=1;text;Radius')
	img = build_qrcode(*parse_params_string('radius=0.5,enhanced_path=1;text;Radius'))
	assert img.radius == 0.5
	assert img.enhanced_path == True


def test_mask():
	qr(get_canvas(), 'mask=1;text;Mask')
	img = build_qrcode(*parse_params_string('mask=1;text;Mask'))
	assert img.mask == True


def test_negative():
	qr(get_canvas(), 'negative=1;text;Negative')
	img = build_qrcode(*parse_params_string('negative=1;text;Negative'))
	assert img.negative == True


def test_alpha():
	qr(get_canvas(), 'negative=1;text;Negative')
	img = build_qrcode(*parse_params_string('fg=#ffffffcc,bg=#ffffff80;text;Negative'))
	assert img.fg_alpha == pytest.approx(0.8, 0.01)
	assert img.bg_alpha == pytest.approx(0.5, 0.01)


def test_custom_error_correction():
	c = get_canvas()
	qr(c, 'error_correction=M;text;Error correction')


def test_unknown_error_correction():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Unknown error correction .*"):
		qr(c, 'error_correction=X;text;Error correction')


def test_custom_version():
	c = get_canvas()
	qr(c, 'version=10;text;Version 10')


def test_not_number_version():
	c = get_canvas()
	with pytest.raises(ValueError, match=r"Version .* is not a number"):
		qr(c, 'version=xx;text;Text')


def test_wrong_area_definition():
	c = get_canvas()
	with pytest.raises(ValueError, match=r".*Wrong value .*, expected coordinates: x:y:w:h"):
		qr(c, 'hole=1cm:2cm;text;Text')


def test_mixed_units():
	c = get_canvas()
	with pytest.raises(ValueError, match=r".*Mixed units in.*"):
		qr(c, 'hole=1cm:2cm:3:4%;text;Text')


def test_area():
	qr(get_canvas(), 'hole=0cm:0cm:5cm:5cm,size=5cm;text;Area')
	img = build_qrcode(*parse_params_string('hole=0cm:0cm:5cm:5cm,size=5cm;text;Area'))
	assert img.hole == [(0, 0, img.width, img.width)]
	qr(get_canvas(), 'hole=1cm:2cm:3cm:1cm,size=5cm;text;Area')
	img = build_qrcode(*parse_params_string('hole=1cm:2cm:3cm:1cm,size=5cm;text;Area'))
	assert img.hole[0][0] == pytest.approx(img.width / 5 * 1, 1)
	assert img.hole[0][1] == pytest.approx(img.width / 5 * 2, 1)
	assert img.hole[0][2] == pytest.approx(img.width / 5 * 3, 1)
	assert img.hole[0][3] == pytest.approx(img.width / 5 * 1, 1)
	qr(get_canvas(), 'hole=20%:40%:60%:20%,size=5cm;text;Area')
	img = build_qrcode(*parse_params_string('hole=20%:40%:60%:20%,size=5cm;text;Area'))
	assert img.hole[0][0] == pytest.approx(img.width / 5 * 1, 1)
	assert img.hole[0][1] == pytest.approx(img.width / 5 * 2, 1)
	assert img.hole[0][2] == pytest.approx(img.width / 5 * 3, 1)
	assert img.hole[0][3] == pytest.approx(img.width / 5 * 1, 1)
	qr(get_canvas(), 'hole=1:2:3:4,size=5cm;text;Area')
	img = build_qrcode(*parse_params_string('hole=1:2:3:4,size=5cm;text;Area'))
	assert img.hole[0][0] == pytest.approx(1, 1)
	assert img.hole[0][1] == pytest.approx(2, 1)
	assert img.hole[0][2] == pytest.approx(3, 1)
	assert img.hole[0][3] == pytest.approx(4, 1)


def get_draw_part_state(img, index=0) -> ReportlabImageBase:
	img = deepcopy(img)
	img.begin_part(img.draw_parts[index])
	return img


def test_unknown_area():
	with pytest.raises(ValueError, match=r"Unknown area .*"):
		get_draw_part_state(build_qrcode(*parse_params_string('draw=notexist;text;All')))


def test_draw_all():
	original_bitmap = build_qrcode(*parse_params_string(';text;All')).bitmap
	all_image = get_draw_part_state(build_qrcode(*parse_params_string('draw=all;text;All')))
	all_image_with_operator = get_draw_part_state(build_qrcode(*parse_params_string('draw=+all;text;All')))
	empty = get_draw_part_state(build_qrcode(*parse_params_string('draw=-all;text;All')))
	assert original_bitmap == all_image.bitmap
	assert original_bitmap == all_image_with_operator.bitmap
	assert sum(empty.bitmap) == 0


def test_draw_eye():
	original_bitmap = build_qrcode(*parse_params_string(';text;All')).bitmap
	eye = get_draw_part_state(build_qrcode(*parse_params_string('draw=eyepupil1;text;All')))
	assert original_bitmap != eye.bitmap
	assert sum(eye.bitmap) == 9


def test_combined_eye():
	eyeball = get_draw_part_state(build_qrcode(*parse_params_string('draw=eyeball1;text;T')))
	eyepupil = get_draw_part_state(build_qrcode(*parse_params_string('draw=eyepupil1;text;T')))
	eye = get_draw_part_state(build_qrcode(*parse_params_string('draw=eye1;text;T')))
	assert sum(eyeball.bitmap) == 24
	assert sum(eyepupil.bitmap) == 9
	assert sum(eye.bitmap) == 9 + 24

	eyeball_combined = get_draw_part_state(build_qrcode(*parse_params_string('draw=eye1-eyepupil1;text;T')))
	eyepupil_combined = get_draw_part_state(build_qrcode(*parse_params_string('draw=eye1-eyeball1;text;T')))
	assert eyeball.bitmap == eyeball_combined.bitmap
	assert eyepupil.bitmap == eyepupil_combined.bitmap

	# alternative form using combined shapes
	eyeball_combined = get_draw_part_state(build_qrcode(*parse_params_string('draw=eye1-eyepupils;text;T')))
	eyepupil_combined = get_draw_part_state(build_qrcode(*parse_params_string('draw=eye1-eyeballs;text;T')))


def test_dont_allow_override_global_options_in_part():
	img = build_qrcode(*parse_params_string('radius=0,padding=0,draw=eye1,radius=1,padding=1;text;T'))
	eye = get_draw_part_state(img)
	assert img.radius == 0
	assert img.padding == 0
	assert eye.radius == 1
	assert img.padding == 0 # don't allow change padding


def test_segments():
	eyeball1 = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyeball1;text;T')))
	eyepupil1 = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyepupil1;text;T')))
	eye1 = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eye1;text;T')))
	for i in range(2, 4):
		eyeball = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyeball{i};text;T')))
		eyepupil = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyepupil{i};text;T')))
		eye = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eye{i};text;T')))
		assert sum(eyeball.bitmap) == 24
		assert sum(eyepupil.bitmap) == 9
		assert sum(eye.bitmap) == 9 + 24
		assert eyeball.bitmap != eyeball1.bitmap
		assert eyepupil.bitmap != eyepupil1.bitmap
		assert eye.bitmap != eye1.bitmap

	eyeballs_sum = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyeball1+eyeball2+eyeball3;text;T')))
	eyepupils_sum = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyepupil1+eyepupil2+eyepupil3;text;T')))
	eyes_sum = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eye1+eye2+eye3;text;T')))
	assert sum(eyeballs_sum.bitmap) == 24 * 3
	assert sum(eyepupils_sum.bitmap) == 9 * 3
	assert sum(eyes_sum.bitmap) == (9 + 24) * 3

	eyeballs = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyeballs;text;T')))
	eyepupils = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyepupils;text;T')))
	eyes = get_draw_part_state(build_qrcode(*parse_params_string(f'draw=eyes;text;T')))
	assert eyeballs_sum.bitmap == eyeballs.bitmap
	assert eyepupils_sum.bitmap == eyepupils.bitmap
	assert eyes_sum.bitmap == eyes.bitmap

	alignballs = get_draw_part_state(build_qrcode(*parse_params_string(f'version=2,draw=alignballs;text;T')))
	alignpupils = get_draw_part_state(build_qrcode(*parse_params_string(f'version=2,draw=alignpupils;text;T')))
	align = get_draw_part_state(build_qrcode(*parse_params_string(f'version=2,draw=align;text;T')))

	assert sum(alignpupils.bitmap) == 1 # single align
	assert sum(alignballs.bitmap) == 16
	assert sum(align.bitmap) == 17


def draw_image(bitmap):
	width = int(math.sqrt(len(bitmap)))
	img = reportlab_image_factory()(border=0, width=width, box_size=1, qrcode_modules=[])
	for address, val in enumerate(bitmap):
		if val:
			img.drawrect(address // width, address % width)
	return img


def test_simple_path():
	# single square
	bitmap = array.array('B', [
		1,
	])

	img = draw_image(bitmap)
	# Outline
	assert img.get_segments() == [[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]]


def test_complex_path():
	bitmap = array.array('B', [
		1, 1,
		1, 0,
	])

	img = draw_image(bitmap)
	assert img.get_segments() == [[(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2), (0, 0)]]


def test_multiple_intersections():
	bitmap = array.array('B', [
		1, 1, 1, 1, 1,
		0, 0, 1, 1, 1,
		0, 0, 1, 0, 1,
		0, 0, 0, 0, 1,
		0, 0, 0, 0, 1,
	])
	img = draw_image(bitmap)
	assert img.get_segments() == [[(0, 0), (5, 0), (5, 5), (4, 5), (4, 2), (3, 2), (3, 3), (2, 3), (2, 1), (0, 1), (0, 0)]]


def test_two_segments():
	bitmap = array.array('B', [
		1, 1, 0, 0, 0,
		1, 1, 0, 0, 0,
		0, 0, 0, 0, 0,
		0, 0, 0, 1, 1,
		0, 0, 0, 1, 1,
	])
	img = draw_image(bitmap)
	assert img.get_segments() == [
		[(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)],
		[(3, 3), (5, 3), (5, 5), (3, 5), (3, 3)],
	]


def test_segment_inside():
	bitmap = array.array('B', [
		1, 1, 1, 1, 1,
		1, 0, 0, 0, 1,
		1, 0, 1, 0, 1,
		1, 0, 0, 0, 1,
		1, 1, 1, 1, 1,
	])
	img = draw_image(bitmap)
	assert img.get_segments() == [
		[(0, 0), (5, 0), (5, 5), (0, 5), (0, 0)],
		[(1, 1), (4, 1), (4, 4), (1, 4), (1, 1)],
		[(2, 2), (3, 2), (3, 3), (2, 3), (2, 2)],
	]


def test_python_api():
	c = get_canvas()
	qr_draw(c, "Text")


def test_python_api_binary_data():
	c = get_canvas()
	qr_draw(c, b"Binary")


def test_python_api_offset():
	c = get_canvas()
	qr_draw(c, "Text", x="1cm", y="1cm", size=5, padding=5)


def test_inverted():
	img_default = build_qrcode(*parse_params_string(';text;Text'))
	img_standard = build_qrcode(*parse_params_string('invert=0;text;Text'))
	img_inverted = build_qrcode(*parse_params_string('invert=1;text;Text'))

	# Default is not inverted
	assert img_default.bitmap == img_standard.bitmap

	for a, b in zip(img_standard.bitmap, img_inverted.bitmap):
		assert a == 1 - b # check if is inverted

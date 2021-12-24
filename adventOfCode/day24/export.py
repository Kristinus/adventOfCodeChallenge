def execute(digits):
	w = x = y = z = 0
    
    w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26 
	z = z // {a} # 1,1,1,1,26,1,26,1,26,26,1,26,26,26,
	x += {b} # 11,14, 10, 14, -8, 14, -11, 10, -6, -9, 12, -5, -4, -9, 
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x 
	y += 1
	z *= y
	y *= 0
	y += w
	y += {c} # 7,8,16,8,3,12,1,8,8,14,4,14,15,6
	y *= x
	z += y
    
    
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z # (w,0,0,0)
	x = x % 26 # (w,0,0,0)
	z = z // 1 # (w,0,0,0)
	x += 11 # (w,11,0,0)
	x = 1 if x == w else 0 # (w,0,0,0)
	x = 1 if x == 0 else 0 # (w,1,0,0)
	y *= 0
	y += 25 # (w,1,25,0)
	y *= x # (w,1,25,0)
	y += 1 # (w,1,26,0)
	z *= y # (w,1,26,0)
	y *= 0 # (w,1,0,0)
	y += w # (w,1,w,0)
	y += 7 # (w,1,w+7,0)
	y *= x # (w,1,w+7,0)
	z += y # (w,1,w+7,w+7)
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0 # (w,0,w+7,z)
	x += z # (w,z,w+7,z)
	x = x % 26 # (w,z % 26,w+7,z)
	z = z // 1
	x += 14 # (w,(z % 26)+14,w+7,z)
	x = 1 if x == w else 0 # (w,0,w+7,z)
	x = 1 if x == 0 else 0 # (w,1,w+7,z)
	y *= 0 # (w,1,0,z)
	y += 25# (w,1,25,z)
	y *= x # (w,1,25,z)
	y += 1 # (w,1,26,z)
	z *= y # (w,1,26,z*26)
	y *= 0 # (w,1,0,z*26)
	y += w # (w,1,w,z*26)
	y += 8 # (w,1,w+8,z*26)
	y *= x # (w,1,w+8,z*26)
	z += y # (w,1,w+8,(z*26)+(w+8))
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 1
	x += 10
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 16
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 1
	x += 14
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 8
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 26
	x += -8
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 3
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 1
	x += 14
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 12
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 26
	x += -11
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 1
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 1
	x += 10
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 8
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 26
	x += -6
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 8
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 26
	x += -9
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 14
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 1
	x += 12
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 4
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 26
	x += -5
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 14
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 26
	x += -4
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 15
	y *= x
	z += y
	print(w,x,y,z)
	w = digits.pop(0)
	x *= 0
	x += z
	x = x % 26
	z = z // 26
	x += -9
	x = 1 if x == w else 0
	x = 1 if x == 0 else 0
	y *= 0
	y += 25
	y *= x
	y += 1
	z *= y
	y *= 0
	y += w
	y += 6
	y *= x
	z += y
	return z
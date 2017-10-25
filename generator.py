import os


def get_file(key):
	file = open(key, 'rb')
	file_content = b'''
HTTP/1.x 200 ok
Content-Type: application/octet-stream

'''
	file_content += file.read()
	file.close()
	return file_content


def get_404():
	content_404 = b'''
HTTP/1.x 404 Page Not Found
Content-Type:text/html

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
<link href="css/decoration.css" rel="stylesheet" >
<link rel="shortcut icon" href="/favicon.ico"/>
<link rel="bookmark" href="/favicon.ico"/>
<title>File System</title>
</head>
<body>
<div class = "ERROR">
<p>404 ERROR</p>
</div>
</body>
</html>
'''
	return content_404


def get_content(key):

	before = b'''
HTTP/1.x 200 ok
Content-Type:text/html

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
<link href="css/decoration.css" rel="stylesheet" >
<link rel="shortcut icon" href="/favicon.ico"/>
<link rel="bookmark" href="/favicon.ico"/>
<title>File System</title>
</head>
<body>
<div class = "container">
'''
	current_dir = os.path.abspath(key)
	#os.path.abspath(os.path.join(os.getcwd(), key))
	#before += '<a href = ' + current_dir + '>' + current_dir + '</a></br></br>'
	before += bytes('<p> '+ current_dir + '</p>', encoding='utf-8')
	path = os.listdir(key)
	for i in path:
		if os.path.isdir(os.path.join(key, i)):
			before += bytes('<a href = ' + i + '>' + '[dir]   ' + i + '</a></br>',encoding='utf-8')
		else:
			before += bytes('<a href = ' + i + '>' + '[file]  ' + i + '</a></br>',encoding='utf-8')
	after = b'''
</div>
</br>
<div>
<a href = "up" ><<<</a>
<div>
</body>
</html>
'''
	main_content = before + after
	return main_content


def get_img():
#img
	file = open('img/vertical-waves.jpg', 'rb')
	pic_content = b'''
HTTP/1.x 200 ok
Content-Type: image/jpg

'''
	pic_content += file.read()
	file.close()
	return pic_content


def get_css():
#css

	file = open('css/decoration.css', 'rb')
	css_content = b'''
HTTP/1.x 200 ok
Content-Type: text/css

'''
	css_content += file.read()
	file.close()
	return css_content


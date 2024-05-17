from django.shortcuts import render


def index(request):
    context = {
        'alamat'    :   'Product',
        'judul'     :   'Halaman product',
        'penjelasan':   'ALL BRANDED',
        'h1'        :   'Sepatu adidas',
        'h2'        :   'Sepatu swalow',
        'h3'        :   'Sepatu nike',
        'h4'        :   'Topi ackerman',
        'h5'        :   'Topi jackloct',
        'h6'        :   'Topi resbery',
        'product1'  :   'img/shoes1.jpg',
        'product2'  :   'img/shoes2.jpg',
        'product3'  :   'img/shoes3.jpg',
        'product4'  :   'img/hat1.jpg',
        'product5'  :   'img/hat2.jpg',
        'product6'  :   'img/hat3.jpg',
    
        
        'nav' : [
            ['shoes/','Shoes'],
            ['hat/','Hat'],
            ['coming_soon/','coming_soon'],
        ]
        
    }
    return render(request, 'index.html',context)

def shoes(request):
    context = {
        'alamat'    :   'Shoes',
        'judul'     :   'Halaman product shoes',
        'penjelasan':   'SHOES BRANDED',
        'h1'        :   'Sepatu adidas',
        'h2'        :   'Sepatu swalow',
        'h3'        :   'Sepatu nike',
        'h4'        :   'Sepatu airjordan',
        'h5'        :   'Sepatu wimcycle',
        'h6'        :   'Sepatu ardiles',
        'product1'  :   'img/shoes4.jpg',
        'product2'  :   'img/shoes5.jpg',
        'product3'  :   'img/shoes6.png',
        'product4'  :   'img/shoes1.jpg',
        'product5'  :   'img/shoes2.jpg',
        'product6'  :   'img/shoes3.jpg',
        
        'nav' : [
            ['/product/shoes','Shoes'],
            ['/product/hat','Hat'],
            ['/product/coming_soon','coming_soon'],
        ]
        
    }
    
    return render(request, 'index.html',context)

def hat(request):
    
    context = {
        'alamat'    :   'Hat',
        'judul'     :   'Halaman product Hat',
        'penjelasan':   'HAT BRANDED',
        'h1'        :   'hat undertaker',
        'h2'        :   'hat coolman',
        'h3'        :   'hat starboy',
        'h4'        :   'hat enjoy',
        'h5'        :   'hat nike',
        'h6'        :   'hat ardiles',
        'product1'  :   'img/hat1.jpg',
        'product2'  :   'img/hat5.jpeg',
        'product3'  :   'img/hat2.jpg',
        'product4'  :   'img/hat3.jpg',
        'product5'  :   'img/hat4.jpg',
        'product6'  :   'img/hat6.jpeg',
        
        'nav' : [
            ['/product/shoes','Shoes'],
            ['/product/hat','Hat'],
            ['/product/coming_soon','coming_soon'],
        ]
    }
    
    return render(request, 'index.html',context)

def coming_soon(request):
    
    context = {
        'alamat'    :   'Soon',
        'judul'     :   'Coming soon product',
        'penjelasan':   'Coming soon',
        'h1'        :   'xxx',
        'h2'        :   'xxx',
        'h3'        :   'xxx',
        'h4'        :   'xxx',
        'h5'        :   'xxx',
        'h6'        :   'xxx',
        'product1'  :   'img/wnext.jpg',
        'product2'  :   'img/wnext.jpg',
        'product3'  :   'img/wnext.jpg',
        'product4'  :   'img/wnext.jpg',
        'product5'  :   'img/wnext.jpg',
        'product6'  :   'img/wnext.jpg',
        
        'nav' : [
            ['/product/shoes','Shoes'],
            ['/product/hat','Hat'],
            ['/product/coming_soon','coming_soon'],
        ]
    }
    
    return render(request, 'index.html',context)

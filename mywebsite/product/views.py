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
            ['/about','about'],
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
            ['about/','about'],
        ]
        
    }
    
    return render(request, 'index.html',context)

def hat(request):
    
    context = {
        'alamat'    :   'Hat',
        'judul'     :   'Halaman product Hat',
        'penjelasan':   'HAT BRANDED',
        'h1'        :   'hat undertaker',
        'h2'        :   'hat swordman',
        'h3'        :   'hat nike',
        'h4'        :   'hat superjoy',
        'h5'        :   'hat distro',
        'h6'        :   'hat kehed',
        'product1'  :   'img/hat4.jpg',
        'product2'  :   'img/hat5.jpeg',
        'product3'  :   'img/hat1.jpg',
        'product4'  :   'img/hat2.jpg',
        'product5'  :   'img/hat3.jpg',
        'product6'  :   'img/hat6.jpeg',
        
        'nav' : [
            ['/product/shoes','Shoes'],
            ['/product/hat','Hat'],
            ['/about','about'],
        ]
    }
    
    return render(request, 'index.html',context)


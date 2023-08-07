# abrindo a imagem - a função cv.imread consegue abrir vários formatos diferentes de imagem
import cv2 as cv
import sys
import numpy as np


def soma(img1, img2):
    altura, largura = img1.shape
    imgSoma = np.add(img1, img2, dtype='int32')
    maior_valor = max(max(linha) for linha in imgSoma)
    menor_valor = min(min(linha) for linha in imgSoma)
    resultado = np.copy(imgSoma)
    if (maior_valor > 255):
        for x in range(altura):
            for y in range(largura):
                a = 255 / (maior_valor - menor_valor)
                b = -a * menor_valor
    return resultado.astype('uint8')


def sub(img1, img2):
    altura, largura = img1.shape
    imgSub = np.subtract(img1, img2, dtype='int32')
    maior_valor = max(max(linha) for linha in imgSub)
    menor_valor = min(min(linha) for linha in imgSub)
    resultado = np.copy(imgSub)
    if (menor_valor < 0):
        for x in range(altura):
            for y in range(largura):
                a = 255 / (maior_valor - menor_valor)
                b = -a * menor_valor
                resultado[y, x] = round(a * imgSub[y, x] + b)
    return resultado.astype('uint8')


def div(img1, img2):
    altura, largura = img1.shape
    imgDiv = np.divide(img1, img2, dtype='float')
    maior_valor = max(max(linha) for linha in imgDiv)
    menor_valor = min(min(linha) for linha in imgDiv)
    resultado = np.copy(imgDiv).astype('uint8')
    for x in range(altura):
        for y in range(largura):
            resultado[y, x] = round(imgDiv[y, x])
    return resultado


def mul(img1, img2):
    altura, largura = img1.shape
    img1 = img1.astype('int32')
    img2 = img2.astype('int32')
    imgMul = img1 * img2
    print(imgMul[0][0])
    maior_valor = max(max(linha) for linha in imgMul)
    menor_valor = min(min(linha) for linha in imgMul)
    resultado = np.copy(imgMul)
    if (maior_valor > 255):
        for x in range(altura):
            for y in range(largura):
                a = 255 / (maior_valor - menor_valor)
                b = -a * menor_valor
                resultado[y, x] = round(a * imgMul[y, x] + b)
    return resultado.astype('uint8')


def logical_and(img1, img2):
    return cv.bitwise_and(img1, img2)


def logical_or(img1, img2):
    return cv.bitwise_or(img1, img2)


def logical_xor(img1, img2):
    return cv.bitwise_xor(img1, img2)


img = cv.imread(cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/lena.pgm"), cv.IMREAD_UNCHANGED)
img2 = cv.imread(cv.samples.findFile(
    "/home/caiovinicius/repos/pdi/Processamento-Digital-de-Imagem/implementacoes/images/caman.tif"), cv.IMREAD_UNCHANGED)
if img is None:
    sys.exit("Could not read the image 1.")
if img2 is None:
    sys.exit("Could not read the image 2.")
print(img[0][0])
print(img2[0][0])
imgSoma = soma(img, img2)
print(imgSoma[0][0])
cv.imshow('soma', soma(img, img2))
multiplicador = np.array([3])
imgMul = mul(img, multiplicador)
cv.imshow('mul', imgMul)
divisor = np.array([3])
cv.imshow('div', div(img, divisor))
cv.imshow('original', img)
print(imgMul[0][0], img[0][0])
cv.imshow('and', logical_and(img, img2))
cv.imshow('or', logical_or(img, img2))
cv.imshow('xor', logical_xor(img, img2))
cv.waitKey()
cv.destroyAllWindows()

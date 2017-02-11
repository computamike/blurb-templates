#!/usr/bin/env python

# -*- coding: utf-8 -*-

import scribus

import math

P = scribus.valueDialog('Book Cover Calculator','Enter Number of pages')

P = float(P)

G = scribus.valueDialog('Book Cover Calculator','Enter Paper Weight (ppi)')

G = float(G)

W = scribus.valueDialog('Book Cover Calculator','Enter Page Width')

W = float(W)

H = scribus.valueDialog('Book Cover Calculator','Enter Page Height')

H = float(H)

R = scribus.valueDialog('Book Cover Calculator','Enter Cover Paper thickness')

R = float(R)

W1 = W

WW = W + 0.125

S = P/G + (R*2)

S = float(S)

W = W + S + W + 0.25

H = H + 0.25

scribus.newDocument((W,H), (0.375, 0.375, 0.375, 0.375), scribus.PORTRAIT, 1,scribus.UNIT_INCHES,scribus.PAGE_1, 0, 1) 

scribus.setVGuides([WW, (W1/2 + 0.125), (WW + S/2), (WW + S), (WW + S + W1/2)])
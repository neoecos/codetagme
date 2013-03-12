# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013  Sebastian Ortiz Vásquez neoecos@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys

params = sys.argv[1:]

if len(params) < 1:
    print("Se espera 1 parámetro.")
else:
    try:
        translateTable = {"i":1,"v":5,"x":10,"l":50,"c":100,"d":500,"m":1000}
        input = params[0].lower()
        sum = 0
        i = 0
        while i < len(input):
            try:
                if(translateTable.get(input[i]) < translateTable.get(input[i+1])):
                    sum += translateTable.get(input[i+1]) - translateTable.get(input[i])
                    i +=2
                else:
                    sum += translateTable.get(input.lower()[i])
                    i += 1
            except IndexError:
                sum += translateTable.get(input.lower()[i])
                i += 1
        print sum		
    except Exception:
        print 'Error'


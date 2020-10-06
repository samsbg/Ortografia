#Autor: Samantha Bautista
#Matricula: A01284462
#Campus: Monterrey
#Fecha: 28 de septiembre de 2020
#Actividad: Proyecto final PISA: ortografia

from tkinter import *
import tkinter as tk
from random import randint
import os

ort = tk.Tk()
ort.title("Ortografía")
ort.geometry("900x500")
ort.resizable(width=False, height=False)
ort.configure(bg="#E4ADBC")


def segundaPagina(b, listaCorrecta, listaIncorrecta):

    global intPuntaje

    titulo.grid(column=2, row=0, columnspan=16, sticky="WNS")

    opcion1 = tk.Button(font=("Avenir Next LT Pro Light (Headings)", 20))
    opcion2 = tk.Button(font=("Avenir Next LT Pro Light (Headings)", 20))

    def comandoSiguiente():
        global intPuntaje
        if intPuntaje == 500:
            regresar()
        else:
            opcion1.grid_forget()
            opcion2.grid_forget()
            creacionDeBotones()

    siguiente = tk.Button(text="Siguiente", bg="#B13B5B", command=comandoSiguiente, font=("Avenir Next LT Pro Light (Headings)", 20), state=DISABLED)
    siguiente.grid(column=14, row=9, columnspan=4, sticky="NSWE", padx=10, pady=10)

    puntaje = tk.Label(text="{}/150".format(intPuntaje),
                       bg="#E4ADBC", font=(None, 20))
    puntaje.grid(column=14, row=2, sticky="E", columnspan=4, padx=10)

    instruccion = tk.Label(text="Selecciona la manera correcta \n de escribir la palabra",
                           bg="#E4ADBC", font=("Avenir Next LT Pro Light (Headings)", 20))
    instruccion.grid(column=4, row=4, columnspan=10, rowspan=2, sticky="NSWE")

    def creacionDeBotones():

        intPalabra = randint(0, (len(listaCorrecta)-1)//2)
        intPosicion = randint(0, 1)

        if (intPosicion == 0):
            opcionPalabra1 = listaCorrecta[intPalabra*2+1]
            opcionPalabra2 = listaIncorrecta[intPalabra*2+1]
        elif (intPosicion == 1):
            opcionPalabra1 = listaIncorrecta[intPalabra*2+1]
            opcionPalabra2 = listaCorrecta[intPalabra*2+1]

        def comandoOpcion(boton):

            global intPuntaje

            if(intPosicion == 0 and boton == 1) or (intPosicion == 1 and boton == 2):
                if(boton == 1):
                    opcion1.configure(bg="green")
                    opcion2.configure(state=DISABLED)

                elif(boton == 2):
                    opcion2.configure(bg="green")
                    opcion1.configure(state=DISABLED)
                intPuntaje = intPuntaje + 10
                listaCorrecta.pop(intPalabra*2)
                listaCorrecta.pop(intPalabra*2)
                listaIncorrecta.pop(intPalabra*2)
                listaIncorrecta.pop(intPalabra*2)
            else:
                if(boton == 1):
                    opcion1.configure(bg="red")
                    opcion2.configure(state=DISABLED)
                elif(boton == 2):
                    opcion2.configure(bg="red")
                    opcion1.configure(state=DISABLED)
                intPuntaje = intPuntaje - 10
                listaCorrecta.append(listaCorrecta[intPalabra*2])
                listaCorrecta.append(listaCorrecta[intPalabra*2+1])
                listaIncorrecta.append(listaIncorrecta[intPalabra*2])
                listaIncorrecta.append(listaIncorrecta[intPalabra*2+1])

            string_Correcto = ""
            string_Incorrecto = ""

            for n in range(len(listaCorrecta)):
                string_Correcto = string_Correcto + listaCorrecta[n] + " "
                string_Incorrecto = string_Incorrecto + \
                    listaIncorrecta[n] + " "

            puntaje.grid_forget()
            puntaje.configure(text="{}/500".format(intPuntaje))
            puntaje.grid(column=14, row=2, sticky="E", columnspan=4, padx=10)
            siguiente.configure(state=NORMAL)

            with open(os.path.abspath("OrtografiaTexto.txt"), 'r',  encoding='utf-8-sig') as f:
                listaDeLineas = f.readlines()
                listaDeLineas[b] = string_Correcto + "\n"
                listaDeLineas[b+8] = string_Incorrecto + "\n"
                puntajesTexto = listaDeLineas[16].split()
                puntajesTexto[b] = str(intPuntaje)


            stringCambio = ""

            for k in puntajesTexto:
                stringCambio = stringCambio + k + " "
            
            listaDeLineas[16] = stringCambio

            with open(os.path.abspath("OrtografiaTexto.txt"), 'w',  encoding='utf-8-sig') as f:
                f.writelines(listaDeLineas)

        opcion1.configure(text=opcionPalabra1, bg="#B13B5B",
                          command=lambda: comandoOpcion(1), state=NORMAL)
        opcion1.grid(column=4, row=7, columnspan=4, sticky="NSWE")

        opcion2.configure(text=opcionPalabra2, bg="#B13B5B",
                          command=lambda: comandoOpcion(2), state=NORMAL)
        opcion2.grid(column=10, row=7, columnspan=4, sticky="NSWE")

        siguiente.configure(state=DISABLED)

    creacionDeBotones()

    def regresar():
        opcion1.grid_forget()
        opcion2.grid_forget()
        puntaje.grid_forget()
        instruccion.grid_forget()
        siguiente.grid_forget()
        primeraPagina()

    regreso.grid(column=0, row=0, columnspan=2, sticky="NSWE")
    regreso.configure(command=regresar)

    for y in range(10):
        ort.grid_rowconfigure(y, weight=1)

    for x in range(18):
        ort.grid_columnconfigure(x, weight=1)


def primeraPagina():
    global boton
    global listaCorrecta
    global listaIncorrecta
    global intPuntaje

    titulo.grid(column=1, row=0, columnspan=5, sticky="WNS")

    def regresar():
        print("Pagina principal")
        ort.destroy()

    regreso.grid(column=0, row=0, sticky="NSWE")
    regreso.configure(command=regresar)

    setLabel = tk.Label(text="Sets", bg="#E4ADBC", font=(None, 20))
    setLabel.grid(column = 2, row =2, columnspan = 2, rowspan = 2)

    def opciones(i):

        global intPuntaje

        for x in range(8):
            listaOpciones[x].grid_forget()
            puntajesLabels[x].grid_forget()
            setLabel.grid_forget()

        correctoString = []
        incorrectoString = []

        with open(os.path.abspath("OrtografiaTexto.txt"), 'r',  encoding='utf-8-sig') as f:
            for x in range(8):
                correctoString.append(f.readline())
            for x in range(8):
                incorrectoString.append(f.readline())

        listaCorrecta = correctoString[i].split()
        listaIncorrecta = incorrectoString[i].split()

        intPuntaje = int(puntajes[i])

        print(i)

        segundaPagina(i, listaCorrecta, listaIncorrecta)

    listaOpciones = []
    puntajesLabels = []

    with open(os.path.abspath("OrtografiaTexto.txt"), 'r',  encoding='utf-8-sig') as f:
        for i in range(16):
            f.readline()
        puntajes = f.readline().split()
    
    for i in range(8):
        listaOpciones.append(tk.Button(text=("Opción", i+1), font=(None, 15), bg="#B13B5B", fg="white", command=lambda i=i: opciones(i)))
        listaOpciones[i].grid(column=(1 + (i % 2)*2), row=(4 + (i//2)*2))

        puntajesLabels.append(
            tk.Label(text="{}/500".format(puntajes[i]), font=(None, 15), bg="#E4ADBC"))
        puntajesLabels[i].grid(column=(2 + (i % 2)*2), row=(4 + (i//2)*2), sticky="EW")

        if(puntajes[i] == 500):
            listaOpciones.configure(state = DISABLED)

    for y in range(11):
        ort.grid_rowconfigure(y, weight=1)

    for x in range(6):
        ort.grid_columnconfigure(x, weight=1)


regreso = tk.Button(text=" 🡄 ", bg="#B13B5B", fg="white", font=(None, 20))
titulo = tk.Label(text="Ortografía", bg="#B13B5B", fg="white", font=(None, 20), width=60)

intPuntaje = 0
boton = 0
listaCorrecta = []
listaIncorrecta = []

if(os.path.exists("OrtografiaTexto.txt") == False):
    with open(os.path.abspath("OrtografiaTexto.txt"), 'w',  encoding='utf-8-sig') as f:
        f.writelines("1. herejía 2. herencia 3. hermanazgo 4. hermosísimo 5. héroes 6. heroico 7. heroína 8. herramientas 9. hervir 10. herbívoro 11. heterogéneo 12. hexágono 13. hidroavión 14. hidrofobia 15. hidroeléctrico 16. hidrógeno 17. hidrografía 18. hidrosfera 19. hiedra 20. hielo 21. hiena 22. hierba 23. hierbabuena 24. hierbal 25. higo 26. hijo 27. hijuelo 28. himno 29. hincapié 30. hindú 31. hipérbaton 32. hipérbole 33. hipersensibilidad 34. hipocondríaco 35. hipocresía 36. hipoglicemia 37. histología 38. histórico-crítico 39. hocico 40. hoguera 41. holgado 42. holgazán 43. hollín 44. hombrecito 45. hombronazo 46. homogéneo 47. homenajear 48. honor 49. honorable 50. honradez\n51. honra 52. honrado 53. hora 54. horizontal 55. hormiguero 56. hortaliza 57. hospedar 58. hospicio 59. hostería 60. hostil 61. hostilidad 62. hoyo 63. hoz 64. hueco 65. huelga 66. huérfano 67. huerto 68. huésped 69. hueso 70. huesecillo 71. huella 72. huevo 73. huevera 74. huidizo 75. huir 76. huida 77. hule 78. humedecer 79. humillar 80. huracán 81. ibero 82. ídem 83. idiosincrasia 84. ignorancia 85. imágenes 86. impávido 87. implícito 88. impresión 89. inalcanzable 90. inauguración 91. incapaz 92. inciso 93. incisión 94. incluso 95. incógnita 96. incompatibilidad 97. incomprensible 98. inconstancia 99. incredibilidad 100. incubar\n101. indecencia 102. indecisión 103. indeciso 104. independencia 105. infancia 106. infinitivo 107. infringir 108. inhabilidad 109. inhalar 110. inherente 111. inhibir 112. inhibición 113. inhospitalario 114. inhumano 115. inhumar 116. inmóvil 117. innovación 118. inocencia 119. insectívoro 120. insignia 121. institutriz 122. insubsistencia 123. inteligente 124. invasión 125. invención 126. invertir 127. investidura 128. investigar 129. invierno 130. invisible 131. irreconciliable 132. ítem 133. jabalí 134. jaqueca 135. jaula 136. jauría 137. Jehová 138. jengibre 139. jeringuilla 140. jeroglífico 141. jesuita 142. jíbaro 143. jilguero 144. jinete 145. jirafa 146. jirones 147. joya 148. joyería 149. jueces 150. jueves\n151. juez 152. jurídico 153. justicia 154. kilómetro 155. ladronzuelo 156. lámpara 157. lampiño 158. lápices 159. látigo 160. lengüetazo 161. leyendo 162. lingüístico 163. libreto 164. licuo 165. ligero 166. linaje 167. linaza 168. línea 169. liricopoético 170. lisonjear 171. literatura 172. llapingacho 173. llavero 174. llovizna 175. logia 176. lombriz 177. longevo 178. longitud 179. luces 180. lloviznar 181. macizo 182. maleable 183. mancebo 184. manguera 185. manirroto 186. maquillaje 187. marfil 188. marítimo 189. mármol 190. masaje 191. mártir 192. matemáticas 193. mayúscula 194. mestizaje 195. migración 196. moho 197. motivo 198. movilidad 199. movilización 200. mujercita\n201. mundano 202. murciélago 203. náutico 204. Nazaret 205. nazco 206. necesito 207. níquel 208. nobiliario 209. nobilísimo 210. nociva 211. nítido 212. nostalgia 213. noviembre 214. núcleo 215. nupcias 216. óbice 217. óbito 218. objeción 219. obsesión 220. obvio 221. occipital 222. occiso 223. oído 224. oigo 225. oír 226. olivar 227. onceavo 228. onceno 229. oquedad 230. ordenador 231. orfandad 232. orca 233. oscilación 234. oscilar 235. ortografía 236. orzuelo 237. ovación 238. oyente 239. ozono 240. paciencia 241. pájaro 242. panfletario 243. parábola 244. paraplejia 245. pararrayos 246. parónimos 247. párrafo 248. pasajero 249. pasear 250. pasividad\n251. pata 252. pavor 253. pavoroso 254. pececillo 255. pedacito 256. pedazos 257. peine 258. pelirrojo 259. pelotazo 260. pelvis 261. peñasco 262. pequeñez 263. percibir 264. perdigón 265. perdiz 266. pereza 267. perezoso 268. pergaminos 269. periódico 270. perseverancia 271. perseverar 272. personaje 273. persuasivo 274. perspicacia 275. pervertir 276. pésame 277. piececillo 278. piececito 279. pijama 280. pingüino 281. pionero 282. piscina 283. pivote 284. plástico 285. plebiscito 286. portalámparas 287. portavoz 288. portazo 289. portezuela 290. posdata 291. posición 292. posoperatorio 293. postiza 294. preciosa 295. precisamente 296. precisión 297. predicción 298. preposición 299. prescindir 300. presidente\n301. presión 302. prevención 303. primavera 304. primicia 305. privilegio 306. probable 307. probeta 308. procaz 309. proceder 310. proceso 311. prohíben 312. prohibido 313. prójimo 314. propicio 315. proposición 316. protagonizar 317. proteger 318. proverbio 319. provisión 320. proyección 321. psicología 322. psicosis 323. puntualizar 324. quehaceres 325. quinceavo 326. quincuagésimo 327. quiromancia 328. quizás 329. ráfaga 330. raíces 331. rapaz 332. realeza 333. reclusión 334. recoger 335. recóndito 336. recruzar 337. rebosar 338. reducción 339. reestructuración 340. reflexión 341. refrigeración 342. regocijo 343. rehacer 344. rehén 345. reír 346. reivindicar 347. rejuvenecer 348. relámpago 349. reloj 350. relojería\n351. renovar 352. resurrección 353. retahíla 354. revalidar 355. reverencia 356. revés 357. revólver 358. rigidez 359. risible 360. robots 361. rodaje 362. rojizo 363. satélite 364. sauce 365. saxofón 366. sazón 367. sedentario 368. seiscientos 369. semáforo 370. semblante 371. semejanza 372. semibreve 373. séptimo 374. septiembre 375. servir 376. sesión 377. setecientos 378. seudónimo 379. sexagenario 380. siesta 381. siete 382. simbolizar 383. revisar 384. revisión 385. sinónimo 386. sintaxis 387. sintonizar 388. sollozo 389. sonríe 390. situación 391. soberano 392. sobrino 393. solemnizar 394. soliviantar 395. solvencia 396. sorbete 397. sosiego 398. suavizar 399.  subconsciente 400. súbito\n1. heregía 2. herensia 3. hermanasgo 4. hermosízimo 5. heroés 6. heróico 7. heroina 8. Herramiéntas 9. herbir 10. hervívoro 11. heterogéno 12. hexagono 13. hidroavion 14. hidrofobía 15. hidroelectríco 16. hidrójeno 17. hidrográfia 18. idrosfera 19. yiedra 20. yelo 21. yena 22. yierba 23. yierbabuena 24. yierbal 25. igo 26. ijo 27. higuelo 28. imno 29. incapié 30. indú 31. hiperbatón 32. híperbole 33. hipersencibilidad 34. hipocondriáco 35. hipocrecía 36. hipoglisemia 37. histólogia 38. historíco-crítico 39. hosico 40. oguera 41. olgado 42. olgazán 43. ollín 44. Hombresito 45. hombronaso 46. homógeneo 47. homenagear 48. onor 49. honoráble 50. honradéz\n51. honrra 52. honrrado 53. hóra 54. horizontál 55. ormiguero 56. hortalisa 57. hozpedar 58. hospisio 59. hoztería 60. hoztil 61. hoztilidad 62. hollo 63. hioz 64. güeco 65. uelga 66. huerfáno 67. güerto 68. huespéd 69. huezo 70. huesesillo 71. hueya 72. güevo 73. güevera 74. huidiso 75. huír 76. huída 77. ule 78. umedecer 79. humiyar 80. hurácan 81. hibero 82. idem 83. idiosincracia 84. ignoransia 85. imagenes 86. impavído 87. implísito 88. impreción 89. incanzable 90. inaugurasión 91. incapas 92. insiso 93. insisión 94. incluzo 95. incogníta 96. inconpatibilidad 97. inconprensible 98. inconstancía 99. incredivilidad 100. incuvar\n101. indecéncia 102. indecición 103. indesiso 104. independensia 105. infáncia 106. infinitibo 107. infrinjir 108. inabilidad 109. inalar 110. inerente 111. inihibir 112. inihibición 113. inospitalario 114. inhumáno 115. inumar 116. inmóbil 117. inovación 118. inosencia 119. insectíboro 120. incignia 121. institutris 122. insubsistensia 123. intelijente 124. invación 125. invensión 126. imvertir 127. inbestidura 128. inbestigar 129. inbierno 130. invicible 131. irreconsiliable 132. item 133. jabali 134. jaqueca 135. jahula 136. jauria 137. Jeová 138. jenjibre 139. geringuilla 140. geroglífico 141. gesuita 142. gíbaro 143. gilguero 144. ginete 145. girafa 146. hirones 147. jolla 148. jollería 149. jueses 150. jueves\n151. jues 152. juridíco 153. justícia 154. kilometro 155. ladronsuelo 156. lampára 157. lampíño 158. lapices 159. latigo 160. lengüetaso 161. lellendo 162. lingüistíco 163. livreto 164. liquo 165. lijero 166. linage 167. linasa 168. linea 169. liricopoetico 170. lisongear 171. literatúra 172. llapingácho 173. llabero 174. llovisna 175. logía 176. lombris 177. lonjevo 178. longitúd 179. luses 180. llovisnar 181. maciso 182. maleáble 183. manzebo 184. mangera 185. maniroto 186. maquillage 187. marfíl 188. maritimo 189. marmol 190. masage 191. martír 192. matematicas 193. mallúscula 194. mestisaje 195. migrasión 196. móho 197. motívo 198. mobilidad 199. mobilización 200. mujersita\n201. mundáno 202. murcielago 203. nautico 204. Nasaret 205. nasco 206. nececito 207. niquél 208. noviliario 209. novilísimo 210. nociba 211. nitído 212. nostálgia 213. noviemvre 214. nucleo 215. nupsias 216. óbise 217. obíto 218. objesión 219. obseción 220. obio 221. ocsipital 222. ocsiso 223. ohído 224. óigo 225. ohír 226. olibar 227. onceabo 228. onseno 229. ocedad 2303. ordenadór 231. horfandad 232. órca 233. ocilación 234. ocilar 235. ortografia 236. orcuelo 237. ovasión 238. ollente 239. osono 240. paciensia 241. págaro 242. panfletário 243. parabola 244. paraplegia 245. pararrallos 246. páronimos 247. parrafo 248. pasagero 249. paséar 250. pasividad\n251. páta 252. pavór 253. pavorozo 254. pecesillo 255. pedasito 256. pedasos 257. péine 258. pelirrójo 259. pelotaso 260. pelviz 261. peñásco 262. pequeñes 263. persibir 264. perdigon 265. perdíz 266. peresa 267. peresoso 268. pergamínos 269. periodico 270. perceverancia 271. perceverar 272. personage 273. persuacivo 274. perspicasia 275. pervertír 276. pesame 277. piecesillo 278. piecesito 279. pijáma 280. pinguino 281. pionéro 282. pisina 283. pibote 284. plastico 285. plebisito 286. portalamparas 287. portavos 288. portaso 289. portesuela 290. posdáta 291. pocición 292. posoperatório 293. postisa 294. presciosa 295. prescisamente 296. presisión 297. predicsión 298. preposisión 299. precindir 300. presidente\n301. preción 302. prevensión 303. primavéra 304. primisia 305. privilejio 306. provable 307. proveta 308. procáz 309. proseder 310. prosceso 311. proíben 312. prohibído 313. prógimo 314. propisio 315. propocición 316. protagonisar 317. protejer 318. proberbio 319. probisión 320. prollección 321. psicolojía 322. psicósis 323. puntualisar 324. queaceres 325. quinceabo 326. quincuagécimo 327. quiromansia 328. quisás 329. rafaga 330. raízes 331. rapáz 332. realesa 333. reclución 334. recojer 335. recondito 336. recrusar 337. rebosár 338. rreducción 339. reestructurasión 340. refleción 341. refrijeración 342. regocigo 343. reacer 344. reén 345. reir 346. reibindicar 347. rejubenecer 348. relampago 349. relój 350. relogería\n351. renobar 352. resurrecsión 353. retaíla 354. rebalidar 355. reberencia 356. rebés 357. revólber 358. rigides 359. ricible 360. robóts 361. rodage 362. rojiso 363. satelite 364. sauze 365. sáxofon 366. sasón 367. cedentário 368. seicientos 369. cemáforo 370. cemblante 371. cemejanza 372. cemibreve 373. céptimo 374. septiemvre 375. serbir 376. seción 377. setesientos 378. ceudónimo 379. cexagenario 380. ciesta 381. ciete 382. simbolisar 383. revizar 384. revición 385. sinonimo 386. cintaxis 387. sintonisar 388. solloso 389. sonrie 390. situasión 391. soverano 392. sovrino 393. solemnisar 394. solibiantar 395. solbencia 396. sorvete 397. sociego 398. suabizar 399.  subconciente 400. subito\n0 0 0 0 0 0 0 0 ")

primeraPagina()

ort.mainloop()

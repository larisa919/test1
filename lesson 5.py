all_iron=5010
one_tool_need=17
one_nail_need=3
print("У нас было", all_iron, "кг железа")
a=all_iron//one_tool_need
print("На изготовление одного инструмента уходит",one_tool_need, "килограмм железа")
print(all_iron,"/",one_tool_need,"=",a, "инструментов мы можем изготовить")
print("На изготовление одного гвоздя уходит",one_nail_need, "килограмма железа" )
b=all_iron%one_tool_need
c=b/one_nail_need
print("Из остатков железа получится",all_iron,"-(",a,"*",one_tool_need,")/",one_nail_need,"=",c, "гвоздей")
d=all_iron-(a*one_tool_need)-b
print("Неиспользованными останутся", all_iron,"-(",a,"*",one_tool_need,")-",b,"=",d, "килограмм железа")
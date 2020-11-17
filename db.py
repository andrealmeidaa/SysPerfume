import sqlite3
path=r'C:\sqlite\databases'
banco=sqlite3.connect(path+r'\dbperfumes.db')
def inserirMarca(nome_marca):
    sql="insert into Marcas (nome) values('{0}')".format(nome_marca)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
def atualizarMarca(id,nome):
    sql="update Marcas set nome='{0}' where id={1}".format(nome,id)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
def localizarMarcaPorNome(nome):
    sql="select * from Marcas where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    marca=cursor.fetchone()
    cursor.close()
    return marca
def listarMarca():
    sql="select * from Marcas"
    cursor=banco.cursor()
    cursor.execute(sql)
    marcas=cursor.fetchall()
    cursor.close()
    return marcas
def listarMarcaNome():
    sql="select nome from Marcas order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_marcas=cursor.fetchall()
    cursor.close()
    marcas=[]
    for nome_marca in nome_marcas:
        marcas.append(nome_marca[0])
    return marcas
def inserirVolume(nome_volume):
    sql="insert into Volumes (nome) values('{0}')".format(nome_volume)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
def atualizarVolume(id,nome):
    sql="update Volumes set nome='{0}' where id={1}".format(nome,id)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
def listarVolume():
    sql="select * from Volumes"
    cursor=banco.cursor()
    cursor.execute(sql)
    volumes=cursor.fetchall()
    cursor.close()
    return volumes
def listarVolumeNome():
    sql="select nome from Volumes order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_volumes=cursor.fetchall()
    cursor.close()
    volumes=[]
    for nome_volume in nome_volumes:
        volumes.append(nome_volume[0])
    return volumes
def localizarVolumePorNome(nome):
    sql="select * from Volumes where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    volume=cursor.fetchone()
    cursor.close()
    return volume
def listarFixacao():
    sql="select * from Fixacoes"
    cursor=banco.cursor()
    cursor.execute(sql)
    fixacoes=cursor.fetchall()
    cursor.close()
    print(len(fixacoes))
    return fixacoes
def localizarFixacaoPorNome(nome):
    sql="select * from Fixacoes where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    fixacao=cursor.fetchone()
    cursor.close()
    return fixacao
def listarFixacaoNome():
    sql="select nome from Fixacoes order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_fixacoes=cursor.fetchall()
    cursor.close()
    fixacoes=[]
    for fixacao in nome_fixacoes:
        fixacoes.append(fixacao[0])
    return fixacoes

def listarPerfumes():
    sql='''
        select Perfumes.id, Perfumes.nome,Perfumes.quantidade,Volumes.nome,Marcas.nome,Fixacoes.nome from 
        Perfumes inner join Volumes on Perfumes.id_volume=Volumes.id 
        inner join Marcas on Perfumes.id_marca=Marcas.id inner join Fixacoes on Perfumes.id_fixacao=Fixacoes.id
    '''
    cursor=banco.cursor()
    cursor.execute(sql)
    perfumes=cursor.fetchall()
    return perfumes
def salvarPerfumes(listaPerfumes):
    cursor=banco.cursor()
    for perfume in listaPerfumes:
        sql=''

        if perfume[0]=='':
            sql="insert into perfumes (nome,quantidade,id_volume,id_marca,id_fixacao) values('{0}',{1},{2},{3},{4})".format(perfume[1],perfume[2],localizarVolumePorNome(perfume[3])[0],
                                                                                                                           localizarMarcaPorNome(perfume[4])[0],localizarFixacaoPorNome(perfume[5])[0]
                                                                                                                            )
        else:
            sql="update perfumes set nome='{1}',quantidade={2},id_volume={3},id_marca={4},id_fixacao={5} where id={0}".format(perfume[0],
                                                                                                                            perfume[1],
                                                                                                                            perfume[2],localizarVolumePorNome(perfume[3])[0],
                                                                                                                           localizarMarcaPorNome(perfume[4])[0],localizarFixacaoPorNome(perfume[5])[0])
        try:
            print(sql)
            cursor.execute(sql)
        except sqlite3.Error as e:
            return False,"Erro ao salvar perfume: "+e.args[0]
    banco.commit()
    cursor.close()
    return True,None


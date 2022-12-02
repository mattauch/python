package com.softgraf.farmacia.repositorio;

import java.io.Serializable;
/*
 * Pacotes para Scopos:
 * javax.faces.bean -> bean JSF
 * javax.faces.view -> bean JSF (PrimeFaces)
 * javax.enterprise.context -> bean CDI (pacote Weld)
 */
import java.util.List;

import javax.enterprise.context.RequestScoped;
import javax.inject.Inject;
import javax.persistence.EntityManager;
//import javax.persistence.EntityTransaction;
import javax.persistence.TypedQuery;

import com.softgraf.farmacia.entity.Produto;
import com.softgraf.farmacia.util.Transacional;



/*
 * Um repositório representa uma coleção de objetos de um tipo específico
 * É um mediador entre a camada de negócios e o acesso de dados
 * Deve fornecer métodos para adicionar, remover, atualizar, buscar, listar, etc.
 */

@RequestScoped // por requisição, informações atualizadas do banco -> menor tempo de vida que
				// atualiza mais rápido.
public class RepositorioProdutos implements Serializable {


	private static final long serialVersionUID = 5812762387203938969L;
	
	
	// Problema: EntityManager não é um Bean CDI, portanto não posso usar @Inject no EntityManager
	private EntityManager em; // comunicação com o banco de dados

	public RepositorioProdutos() { // construtor padrão
	}
	
	@Inject // Problema: EntityManager não é um Bean CDI, portanto não posso usar @Inject no EntityManager
	public RepositorioProdutos(EntityManager em) {
	this.em = em;
	}
	
	@Transacional
	public void adicionar(Produto produto) {
	//	EntityTransaction tx = em.getTransaction();
	//	tx.begin();
		em.persist(produto);
	//	tx.commit();
	}
	
	@Transacional
	public void removerPorId(Integer id) {
		Produto produto = em.find(Produto.class, id); // traz o cliente da classe Cliente
		
		em.remove(produto);
	}
	
	
	public Produto buscarPorId(Integer id) {
		return em.find(Produto.class, id);
	}
	
	@Transacional
	public void atualizar(Produto produto) {
		em.merge(produto); // merge = juntar = atualizar
	}

	public List<Produto> todos() {
		// JPQL (JPA Querry Language) -> busca na entidade, diferente do SQL que busca
		// no banco.
		TypedQuery<Produto> query = em.createQuery("from Produto ", Produto.class); 																		
		return query.getResultList();

	
	}

}

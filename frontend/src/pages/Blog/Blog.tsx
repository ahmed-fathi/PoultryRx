import React from 'react'
import { useQuery } from '@tanstack/react-query'
import { fetchBlog } from '../../services/mockApi'
import ArticleCard from '../../components/ArticleCard'

export default function Blog() {
  const { data } = useQuery(['blog'], () => fetchBlog(1, 20))

  return (
    <section className="blog-page">
      <h1>Blog</h1>
      <div className="article-list">
        {data?.results.map((a: any) => (
          <ArticleCard key={a.id} article={a} />
        ))}
      </div>
    </section>
  )
}

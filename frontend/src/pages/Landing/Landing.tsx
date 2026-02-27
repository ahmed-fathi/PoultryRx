import React from 'react'
import { useQuery } from '@tanstack/react-query'
import { fetchFeatured, fetchTools } from '../../services/mockApi'
import ArticleCard from '../../components/ArticleCard'

export default function Landing() {
  const { data: featured } = useQuery(['featured'], fetchFeatured)
  const { data: tools } = useQuery(['tools'], fetchTools)

  return (
    <section className="landing-page">
      <h1>Featured Articles</h1>
      <div className="featured-list">
        {featured?.articles.map((a: any) => (
          <ArticleCard key={a.id} article={a} />
        ))}
      </div>

      <h2>AI Tools</h2>
      <div className="tools-list">
        {tools?.results.map((t: any) => (
          <div key={t.id} className="tool-card">{t.name}</div>
        ))}
      </div>
    </section>
  )
}

import React from 'react'
import { Link } from 'react-router-dom'
import '../../styles/components/_article-card.scss'

export default function ArticleCard({ article }: { article: any }) {
  return (
    <article className="article-card">
      <Link to={`/articles/${article.slug}`}>
        <img src={article.cover_image} alt={article.title} />
        <h3>{article.title}</h3>
        <p>{article.excerpt}</p>
      </Link>
    </article>
  )
}

import React from 'react'
import { useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { fetchArticle } from '../../services/mockApi'

export default function Article() {
  const { slug } = useParams()
  const { data } = useQuery(['article', slug], () => fetchArticle(slug || ''))

  if (!data) return <div>Loading...</div>

  return (
    <article className="article-detail">
      <h1>{data.title}</h1>
      <div className="meta">By {data.author.username} — {data.publish_date}</div>
      <div className="content" dangerouslySetInnerHTML={{ __html: data.content }} />
    </article>
  )
}

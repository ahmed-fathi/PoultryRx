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
      {/*
        SECURITY NOTE: dangerouslySetInnerHTML is used here with mock/fixture data only.
        In production, all HTML content MUST be sanitised server-side (e.g. with DOMPurify
        or a server-side allow-list sanitiser) before being stored and served. The API layer
        is responsible for ensuring no unsanitised user-supplied HTML reaches this component.
      */}
      <div className="content" dangerouslySetInnerHTML={{ __html: data.content }} />
    </article>
  )
}

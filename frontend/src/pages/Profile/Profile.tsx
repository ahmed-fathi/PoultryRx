import React from 'react'
import { useParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { fetchProfile } from '../../services/api'

export default function Profile() {
  const { username } = useParams()
  const { data } = useQuery(['profile', username], () => fetchProfile(username || ''))

  if (!data) return <div>Loading...</div>

  return (
    <section className="profile-page">
      <h1>{data.username}</h1>
      <div>{data.first_name} {data.last_name}</div>
      <div>Public articles: {data.public_articles_count}</div>
      <div>Total reads: {data.total_read_count}</div>
    </section>
  )
}


import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'
import Landing from './pages/Landing/Landing'
import Blog from './pages/Blog/Blog'
import Article from './pages/Article/Article'
import Profile from './pages/Profile/Profile'
import Library from './pages/Library/Library'
import About from './pages/About/About'
import FAQ from './pages/FAQ/FAQ'

export default function App() {
  return (
    <div className="app-root">
      <header className="site-header">
        <nav>
          <Link to="/">Home</Link> | <Link to="/blog">Blog</Link> | <Link to="/library">Library</Link> | <Link to="/about">About</Link> | <Link to="/faq">FAQ</Link>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/blog" element={<Blog />} />
          <Route path="/articles/:slug" element={<Article />} />
          <Route path="/profiles/:username" element={<Profile />} />
          <Route path="/library" element={<Library />} />
          <Route path="/about" element={<About />} />
          <Route path="/faq" element={<FAQ />} />
        </Routes>
      </main>
    </div>
  )
}

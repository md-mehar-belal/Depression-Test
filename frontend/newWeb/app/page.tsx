'use client'

import React from 'react'
import { useAuth } from '@/lib/auth-context'
import { useRouter } from 'next/navigation'
import { Button } from '@/components/ui/button'
import { Card, CardContent } from '@/components/ui/card'
import { Leaf, Heart, Brain, TrendingUp } from 'lucide-react'
import Link from 'next/link'

export default function HomePage() {
  const { isAuthenticated, loading } = useAuth()
  const router = useRouter()

  React.useEffect(() => {
    if (!loading && isAuthenticated) {
      router.push('/dashboard')
    }
  }, [isAuthenticated, loading, router])

  return (
    <div className="min-h-screen bg-gradient-to-b from-background via-background to-muted">
      {/* Navigation */}
      <nav className="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="h-8 w-8 rounded-lg bg-gradient-to-br from-primary to-secondary flex items-center justify-center">
                <Heart className="h-5 w-5 text-white" />
              </div>
              <span className="font-bold text-lg">MindWell</span>
            </div>
            <div className="flex gap-4">
              <Link href="/auth/login">
                <Button variant="ghost">Sign In</Button>
              </Link>
              <Link href="/auth/signup">
                <Button>Get Started</Button>
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 sm:py-32">
        <div className="text-center space-y-8">
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-foreground text-balance">
            Understand Your Emotional Well-Being
          </h1>
          <p className="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto text-balance">
            Take evidence-based mental health assessments developed by medical professionals. Get compassionate support and personalized guidance.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-8">
            <Link href="/auth/signup">
              <Button size="lg" className="w-full sm:w-auto">
                Start Free Assessment
              </Button>
            </Link>
            <Button size="lg" variant="outline" className="w-full sm:w-auto">
              Learn More
            </Button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-foreground mb-4">
            Comprehensive Assessment Tools
          </h2>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            Choose from multiple evidence-based assessment methods to understand your mental health better.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Card className="hover:shadow-lg transition-shadow">
            <CardContent className="p-8 space-y-4">
              <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center">
                <Brain className="h-6 w-6 text-primary" />
              </div>
              <h3 className="font-semibold text-lg">PHQ-9 Assessment</h3>
              <p className="text-muted-foreground">
                The widely-used Patient Health Questionnaire to screen for depression. Quick and reliable.
              </p>
              <p className="text-sm text-secondary font-medium">9 Questions • 5 minutes</p>
            </CardContent>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardContent className="p-8 space-y-4">
              <div className="h-12 w-12 rounded-lg bg-secondary/10 flex items-center justify-center">
                <TrendingUp className="h-6 w-6 text-secondary" />
              </div>
              <h3 className="font-semibold text-lg">BDI-II Assessment</h3>
              <p className="text-muted-foreground">
                Beck Depression Inventory-II provides deeper insight into depressive symptoms and severity.
              </p>
              <p className="text-sm text-secondary font-medium">21 Questions • 10 minutes</p>
            </CardContent>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardContent className="p-8 space-y-4">
              <div className="h-12 w-12 rounded-lg bg-accent/10 flex items-center justify-center">
                <Leaf className="h-6 w-6 text-accent" />
              </div>
              <h3 className="font-semibold text-lg">CES-D Assessment</h3>
              <p className="text-muted-foreground">
                Center for Epidemiologic Studies Depression Scale for comprehensive emotional evaluation.
              </p>
              <p className="text-sm text-secondary font-medium">20 Questions • 5 minutes</p>
            </CardContent>
          </Card>

          <Card className="hover:shadow-lg transition-shadow">
            <CardContent className="p-8 space-y-4">
              <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center">
                <Heart className="h-6 w-6 text-primary" />
              </div>
              <h3 className="font-semibold text-lg">AI-Powered Assessment</h3>
              <p className="text-muted-foreground">
                Our intelligent algorithm provides personalized evaluation based on modern AI technology.
              </p>
              <p className="text-sm text-secondary font-medium">8 Questions • 5 minutes</p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Benefits Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 bg-gradient-to-r from-primary/5 to-secondary/5 rounded-2xl my-20">
        <div className="text-center mb-16">
          <h2 className="text-3xl sm:text-4xl font-bold text-foreground mb-4">
            Why Choose MindWell?
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="space-y-4">
            <h3 className="font-semibold text-lg">Evidence-Based</h3>
            <p className="text-muted-foreground">
              All our assessments are backed by clinical research and validated by mental health professionals.
            </p>
          </div>
          <div className="space-y-4">
            <h3 className="font-semibold text-lg">Compassionate Support</h3>
            <p className="text-muted-foreground">
              We approach mental health with empathy and understanding, never judgment or stigma.
            </p>
          </div>
          <div className="space-y-4">
            <h3 className="font-semibold text-lg">Privacy First</h3>
            <p className="text-muted-foreground">
              Your data is secure and confidential. We never share your information without consent.
            </p>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
        <h2 className="text-3xl sm:text-4xl font-bold text-foreground mb-6 text-balance">
          Ready to understand yourself better?
        </h2>
        <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto text-balance">
          Take the first step toward better mental health today. It takes just a few minutes.
        </p>
        <Link href="/auth/signup">
          <Button size="lg">
            Start Your Free Assessment Now
          </Button>
        </Link>
      </section>

      {/* Footer */}
      <footer className="border-t border-border bg-card/50 backdrop-blur-sm mt-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div>
              <h3 className="font-semibold mb-4">Product</h3>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground">Features</a></li>
                <li><a href="#" className="hover:text-foreground">Assessments</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Company</h3>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground">About</a></li>
                <li><a href="#" className="hover:text-foreground">Blog</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Legal</h3>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground">Privacy</a></li>
                <li><a href="#" className="hover:text-foreground">Terms</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold mb-4">Support</h3>
              <ul className="space-y-2 text-sm text-muted-foreground">
                <li><a href="#" className="hover:text-foreground">Help Center</a></li>
                <li><a href="#" className="hover:text-foreground">Contact</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-border pt-8 text-center text-sm text-muted-foreground">
            <p>&copy; 2024 MindWell. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

import React from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { TestResult } from '@/lib/types'
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'
import { CheckCircle2, Info } from 'lucide-react'

interface ResultCardProps {
  testName: string
  result: TestResult
}

const severityColors = {
  low: 'border-green-200 bg-green-50',
  moderate: 'border-amber-200 bg-amber-50',
  elevated: 'border-orange-200 bg-orange-50',
  high: 'border-red-200 bg-red-50',
}

const severityBadgeColors = {
  low: 'bg-green-100 text-green-800',
  moderate: 'bg-amber-100 text-amber-800',
  elevated: 'bg-orange-100 text-orange-800',
  high: 'bg-red-100 text-red-800',
}

export function ResultCard({ testName, result }: ResultCardProps) {
  return (
    <div className="space-y-6">
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>{testName} Results</CardTitle>
              <CardDescription>Your assessment results and interpretation</CardDescription>
            </div>
            <div className={`px-4 py-2 rounded-full text-sm font-semibold ${severityBadgeColors[result.severity]}`}>
              {result.severity.charAt(0).toUpperCase() + result.severity.slice(1)}
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-6">
          <div>
            <h3 className="text-sm font-semibold text-muted-foreground mb-2">Score</h3>
            <p className="text-3xl font-bold text-primary">{result.score}</p>
          </div>

          <Alert className={`border-2 ${severityColors[result.severity]}`}>
            <Info className="h-4 w-4" />
            <AlertTitle>Assessment Result</AlertTitle>
            <AlertDescription>{result.interpretation}</AlertDescription>
          </Alert>

          <div>
            <h3 className="text-sm font-semibold text-foreground mb-3">Recommended Next Steps</h3>
            <ul className="space-y-2">
              {result.recommendations.map((recommendation, index) => (
                <li key={index} className="flex items-start gap-3">
                  <CheckCircle2 className="h-5 w-5 text-secondary flex-shrink-0 mt-0.5" />
                  <span className="text-sm text-foreground">{recommendation}</span>
                </li>
              ))}
            </ul>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

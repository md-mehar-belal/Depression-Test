# MindWell - Depression Assessment Platform

A modern, responsive React-based frontend for mental health assessments featuring evidence-based screening tests including PHQ-9, BDI-II, CES-D, and an AI-powered assessment tool.

## Features

### Assessment Tools
- **PHQ-9**: Patient Health Questionnaire-9 (9 questions, ~5 minutes)
- **BDI-II**: Beck Depression Inventory-II (21 questions, ~10 minutes)
- **CES-D**: Center for Epidemiologic Studies Depression Scale (20 questions, ~5 minutes)
- **AI-Powered Assessment**: Intelligent 8-question evaluation

### Core Functionality
- ✅ User authentication (email/password, Google OAuth ready)
- ✅ Comprehensive dashboard with quick stats
- ✅ Interactive test interface with progress tracking
- ✅ Immediate result calculation with interpretations
- ✅ Personalized recommendations based on scores
- ✅ User profile management
- ✅ Responsive design (mobile-first)
- ✅ Accessibility-first (WCAG 2.1 AA)

### Design & UX
- Clean, modern medical-grade interface
- White primary background with balanced blue/green accents
- Compassionate, non-alarming messaging
- Smooth animations and transitions
- Full keyboard navigation support
- High contrast for accessibility

### Code Quality
- Built with React 18 + Next.js 16 + TypeScript
- React Hook Form + Zod for validation
- Context API for state management
- Functional components with hooks only
- Comprehensive error handling
- Client and server-side validation
- Security-first approach

## Project Structure

```
app/
├── auth/
│   ├── login/
│   ├── signup/
│   └── forgot-password/
├── tests/
│   └── [testType]/
├── dashboard/
├── profile/
├── layout.tsx
├── page.tsx (landing)
└── globals.css

lib/
├── types.ts              # TypeScript interfaces
├── schemas.ts            # Zod validation schemas
├── test-data.ts          # Test questions & scoring logic
├── auth-context.tsx      # Authentication state
└── api-client.ts         # Axios instance

components/
├── form-field.tsx        # Reusable form input wrapper
├── test-card.tsx         # Test selection card
├── result-card.tsx       # Result display
└── ui/                   # shadcn/ui components
```

## Getting Started

### Prerequisites
- Node.js 18+ or bun
- pnpm (or npm/yarn)

### Installation

1. **Clone and Install**
```bash
# Install dependencies
pnpm install
```

2. **Environment Setup**
```bash
# Copy the example environment file
cp .env.local.example .env.local

# Update .env.local with your configuration
# NEXT_PUBLIC_API_URL=http://localhost:3001/api
```

3. **Start Development Server**
```bash
pnpm dev
```

The app will be available at `http://localhost:3000`

## Usage

### User Flow

1. **Landing Page** (`/`)
   - Overview of assessment tools
   - Sign up / Sign in links
   - Feature highlights

2. **Authentication**
   - Sign up: `/auth/signup`
   - Login: `/auth/login`
   - Forgot password: `/auth/forgot-password`

3. **Dashboard** (`/dashboard`)
   - View all available tests
   - Quick stats (tests completed, last assessment)
   - Recent results

4. **Test Interface** (`/tests/[testType]`)
   - Start screen with test info
   - Interactive questions with progress bar
   - Immediate scoring and results
   - Personalized recommendations

5. **Profile** (`/profile`)
   - View account information
   - Update profile settings
   - Security options
   - Sign out

## Testing the App

### With Mock Data (No Backend Required)

The app works entirely with client-side logic for assessment calculation. You can:

1. Use the test interface without authentication by modifying `useAuth()` checks
2. All test questions, scoring logic, and interpretations are included
3. Results are calculated immediately on form submission

### API Integration (Backend Required)

To fully integrate with a backend:

1. Implement endpoints for:
   - `POST /auth/login`
   - `POST /auth/signup`
   - `GET /auth/me`
   - `POST /auth/logout`
   - `POST /auth/forgot-password`
   - `POST /auth/reset-password`
   - `POST /auth/google`
   - `POST /tests/submit`
   - `GET /tests/history`
   - `GET /profile`
   - `PUT /profile`

2. Update the API base URL in `.env.local`

3. Modify `useAuth()` context to match your API responses

## Validation & Security

### Frontend Validation
- React Hook Form for form state
- Zod schemas for validation
- Real-time error feedback
- Field-level validation rules

### Backend Validation (Required)
- Always validate on the server
- Sanitize input to prevent XSS
- Use parameterized queries for SQL
- Implement rate limiting on sensitive endpoints
- Never expose internal errors

### Authentication
- JWT token stored securely (currently in localStorage - should use httpOnly cookies)
- Token validation on app load
- Auto-logout on token expiration
- Protected routes via `useAuth()` context

## Styling & Customization

### Theme System
All colors are defined as CSS custom properties in `app/globals.css`:

```css
--primary: oklch(0.455 0.166 258.9)  /* Medical Blue */
--secondary: oklch(0.547 0.136 142.456)  /* Calming Green */
--accent: oklch(0.7 0.15 205.4)  /* Cyan highlights */
```

### Tailwind Configuration
Uses shadcn/ui new-york style with custom medical theme. All components use semantic tokens:
- `bg-background`, `text-foreground`
- `bg-card`, `text-card-foreground`
- `bg-primary`, `text-primary-foreground`
- etc.

### Customization
1. Update color tokens in `app/globals.css`
2. Modify component styles in `components/ui/`
3. Use Tailwind's responsive prefixes for layouts

## Accessibility

Features included:
- ✅ Semantic HTML (button, form, labels)
- ✅ ARIA labels where needed
- ✅ Keyboard navigation support
- ✅ Focus indicators on interactive elements
- ✅ High contrast ratios (WCAG AA)
- ✅ Form labels associated with inputs
- ✅ Error messages linked to inputs
- ✅ Skip links for main content

## Performance Optimization

- Lazy-loaded route pages with React.lazy()
- Optimized images and assets
- Proper dependency arrays in useEffect/useMemo
- No unnecessary re-renders
- Code splitting by route

## Mental Health & Messaging Guidelines

### Tone
- Supportive and compassionate
- Professional yet approachable
- Non-judgmental language
- Evidence-based terminology

### Examples
✅ **Good**: "Elevated depressive indicators detected"
❌ **Bad**: "You are mentally ill"

✅ **Good**: "Support resources available"
❌ **Bad**: "Seek help immediately" (alarming)

✅ **Good**: "Consider speaking with a professional"
❌ **Bad**: "You need therapy" (prescriptive)

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Development

### Code Style
- Functional components only (no class components)
- Hooks-based patterns
- Descriptive variable names
- Small, focused functions
- No duplication (DRY principle)

### Common Tasks

**Add a new test type:**
1. Add `TestType` to `lib/types.ts`
2. Add questions to `lib/test-data.ts`
3. Add scoring logic to `calculateTestScore()`
4. Update `testInfo` object
5. No page changes needed (uses dynamic routing)

**Update validation schema:**
1. Modify schema in `lib/schemas.ts`
2. Update form component
3. Ensure server validates the same rules

**Modify theme colors:**
1. Update CSS variables in `app/globals.css`
2. Colors cascade to all components automatically

## Known Limitations

- Backend API not included (mock-friendly for now)
- localStorage used for auth tokens (should use httpOnly cookies)
- No test history persistence yet (would require backend)
- Google OAuth setup required for that feature
- Email verification disabled by default

## Future Enhancements

- [ ] Backend API integration
- [ ] Test history and trend analysis
- [ ] Export results as PDF
- [ ] Integration with mental health resources
- [ ] Multi-language support
- [ ] Dark mode support
- [ ] Social sharing of resources
- [ ] Professional provider connections

## Support & Resources

### Mental Health Crisis Resources
- **National Suicide Prevention Lifeline**: 988 (US)
- **Crisis Text Line**: Text HOME to 741741
- **International Association for Suicide Prevention**: https://www.iasp.info/resources/Crisis_Centres/

### Technical Support
- Review component documentation in the code
- Check TypeScript interfaces for data structures
- Validate against test-data.ts for assessment details

## License

This project is provided as-is for mental health assessment purposes.

## Disclaimer

This application is designed for educational and screening purposes only. It is not a substitute for professional mental health evaluation or treatment. Users experiencing mental health concerns should consult with qualified healthcare providers. The assessments provided here are screening tools only and should not be used for diagnosis or treatment planning without professional consultation.

## Contributing

Contributions are welcome! Please ensure:
- Maintain accessibility standards
- Follow the code style guidelines
- Use compassionate, non-alarming language
- Add proper TypeScript types
- Include form validation
- Test keyboard navigation

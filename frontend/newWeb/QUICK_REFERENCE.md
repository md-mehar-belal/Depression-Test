# MindWell - Quick Reference Guide

Fast answers to common questions about the platform.

---

## 🚀 Getting Started (30 seconds)

```bash
# 1. Install
pnpm install

# 2. Run
pnpm dev

# 3. Visit
http://localhost:3000
```

That's it! The app is live and ready to use.

---

## 📍 Key URLs

| Page | URL | Description |
|------|-----|-------------|
| Landing | `/` | Public homepage |
| Sign Up | `/auth/signup` | Create account |
| Login | `/auth/login` | Sign in |
| Forgot Password | `/auth/forgot-password` | Password recovery |
| Dashboard | `/dashboard` | Main app (protected) |
| PHQ-9 Test | `/tests/phq9` | 9-question test |
| BDI-II Test | `/tests/bdi2` | 21-question test |
| CES-D Test | `/tests/cesd` | 20-question test |
| AI Test | `/tests/ai-test` | 8-question test |
| Profile | `/profile` | User settings (protected) |

---

## 🔐 Testing Without Backend

**The app works WITHOUT any backend server!**

```javascript
// Mock login - just navigate to /dashboard after signup
// All test calculations work client-side
// Results display immediately
```

**To test:**
1. Sign up with any email/password
2. Complete a test
3. See results instantly

No API needed for demonstrations or learning.

---

## 📝 Adding a New Test

### Step 1: Update Type
```typescript
// lib/types.ts
export type TestType = '...' | 'my-test'
```

### Step 2: Add Questions
```typescript
// lib/test-data.ts
'my-test': [
  {
    id: 'my_1',
    text: 'Question?',
    options: [
      { value: 0, label: 'Answer 1' },
      { value: 1, label: 'Answer 2' },
      // ...
    ]
  }
  // More questions...
]
```

### Step 3: Add Scoring
```typescript
// In calculateTestScore()
case 'my-test': {
  if (score <= 10) {
    category = 'minimal'
    severity = 'low'
    // Set interpretation & recommendations
  }
  // ... more score ranges
  break
}
```

### Step 4: Add Test Info
```typescript
// In testInfo
'my-test': {
  name: 'My Test Name',
  description: 'Description',
  duration: '5-10 minutes',
  questions: 20,
}
```

**Done!** Test auto-appears on dashboard. Dynamic routing handles everything.

---

## 🎨 Changing Colors

All colors are in one file:

```css
/* app/globals.css */
:root {
  --primary: oklch(0.455 0.166 258.9);     /* Blue */
  --secondary: oklch(0.547 0.136 142.456); /* Green */
  --accent: oklch(0.7 0.15 205.4);         /* Cyan */
  /* ... more colors ... */
}
```

**To change theme:**
1. Open `app/globals.css`
2. Update the color values
3. All components update automatically (semantic tokens)
4. No component changes needed

---

## 🔌 Backend Integration Checklist

### Required Endpoints
- [ ] `POST /auth/signup` - Create account
- [ ] `POST /auth/login` - Authenticate
- [ ] `GET /auth/me` - Get current user
- [ ] `POST /auth/logout` - Logout
- [ ] `POST /auth/forgot-password` - Reset password
- [ ] `POST /tests/submit` - Submit test
- [ ] `GET /tests/history` - Get results
- [ ] `PUT /profile` - Update profile

### Setup Steps
1. Update `NEXT_PUBLIC_API_URL` in `.env.local`
2. Implement endpoints with same Zod schemas
3. Hash passwords securely (bcrypt)
4. Return JWT tokens on auth
5. Validate tokens on protected endpoints

### Validation
```typescript
// Use same schemas from lib/schemas.ts
import { loginSchema } from '@/lib/schemas'

// Frontend + Backend validation
// Frontend: React Hook Form + Zod
// Backend: Same Zod schema validation
```

---

## 📊 Test Scoring Quick Reference

| Test | Questions | Range | Min | Max | Scoring |
|------|-----------|-------|-----|-----|---------|
| PHQ-9 | 9 | 0-27 | 0-4 (Minimal) | 20-27 (Severe) | Points/question: 0-3 |
| BDI-II | 21 | 0-63 | 0-13 (Minimal) | 43-63 (Severe) | Points/item: 0-3 |
| CES-D | 20 | 0-60 | 0-15 (Minimal) | 50-60 (Severe) | Points/item: 0-3 |
| AI Test | 8 | 0-24 | 0-6 (Minimal) | 21-24 (Severe) | Points/q: 0-3 |

**All tests have 4 severity levels:**
- 🟢 Low: Minimal indicators
- 🟡 Moderate: Mild to moderate indicators
- 🟠 Elevated: Moderately severe indicators
- 🔴 High: Severe indicators

---

## 🛡️ Security Essentials

### ✅ Implemented
- JWT token authentication
- Protected routes
- Form validation
- Error handling

### ⚠️ Required (Backend)
- Password hashing (bcrypt minimum)
- Secure token generation
- HTTPS only
- CORS configuration
- Rate limiting on auth endpoints
- SQL injection prevention (parameterized queries)
- Input sanitization

### 🔑 Environment Variables
```bash
NEXT_PUBLIC_API_URL=http://your-api.com
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-id  # Optional
```

**NEVER commit real values!** Use `.env.local` which is gitignored.

---

## 🧪 Test Result Examples

### Low Score (PHQ-9: 2)
```
Score: 2
Interpretation: "Minimal depressive indicators detected."
Recommendations:
- Continue healthy lifestyle habits
- Stay connected with supportive relationships
- Engage in regular physical activity
```

### Moderate Score (PHQ-9: 12)
```
Score: 12
Interpretation: "Moderate depressive indicators detected. 
Professional support may be beneficial."
Recommendations:
- Consider speaking with a mental health professional
- Establish a daily routine
- Prioritize self-care and rest
- Connect with support groups or communities
```

### Severe Score (PHQ-9: 24)
```
Score: 24
Interpretation: "Severe depressive indicators detected. 
Professional mental health support is important."
Recommendations:
- Contact a mental health professional immediately
- Reach out to a crisis helpline if needed
- Talk to your doctor about treatment options
- Build a strong support network around you
```

---

## 📱 Responsive Design

### Mobile (< 640px)
- Single column layouts
- Full-width buttons
- Large touch targets (44x44px)
- Stacked navigation

### Tablet (640px - 1024px)
- 2-column grids
- Optimized spacing
- Readable font sizes
- Accessible navigation

### Desktop (> 1024px)
- Multi-column layouts
- Enhanced spacing
- Optimized typography
- Rich interactions

**All handled automatically via Tailwind prefixes** (`sm:`, `md:`, `lg:`).

---

## 🎯 Common Customizations

### Change Button Colors
```tsx
// In component
<Button className="bg-secondary">Click me</Button>

// Or in globals.css
--primary: your-new-color
```

### Add New Question Type
See "Adding a New Test" section above.

### Modify Form Fields
```tsx
// Edit app/auth/signup/page.tsx
// Or copy pattern to new form page
```

### Update Landing Page Copy
```tsx
// Edit app/page.tsx
// All text is editable JSX
```

### Change Error Messages
```typescript
// Edit lib/schemas.ts
const schema = z.object({
  field: z.string().min(1, 'Your custom message here')
})
```

---

## 🔍 Debugging Tips

### Console Logs (Already Helpful)
The app uses minimal console output. For debugging:

```typescript
// Add during development
console.log('[v0] Debug info:', variable)
// Remove before production
```

### Check Auth State
```typescript
// In component
const { user, isAuthenticated, loading } = useAuth()
console.log({ user, isAuthenticated, loading })
```

### Test Validation
```typescript
// Try submitting form with invalid data
// Error messages appear below fields
```

### Check Network
Press F12 → Network tab to see:
- Failed API calls (show what would be needed)
- Response payloads
- Request headers

### Browser Storage
Press F12 → Application → Local Storage:
- See stored auth token
- Check other persisted data

---

## 📚 File Reference

### Most Important Files
- `app/page.tsx` - Landing page (start here)
- `app/tests/[testType]/page.tsx` - Test logic
- `lib/test-data.ts` - All questions & scoring
- `lib/auth-context.tsx` - Auth logic
- `app/globals.css` - Theme colors

### Documentation
- `README.md` - Full technical docs
- `GETTING_STARTED.md` - User walkthrough
- `DEVELOPMENT.md` - Developer deep-dive
- `BUILD_SUMMARY.md` - Project overview

### Components (Copy patterns from these)
- `components/form-field.tsx` - Form wrapper
- `components/test-card.tsx` - Card component
- `app/auth/login/page.tsx` - Form page pattern
- `app/dashboard/page.tsx` - Dashboard pattern

---

## ⚡ Performance Tips

### Fast Development
```bash
pnpm dev  # HMR auto-updates
```

### Fast Builds
```bash
pnpm run build  # Vercel deployment-ready
```

### Monitor Bundle
```bash
npm run build -- --analyze  # See bundle breakdown
```

### Code Splitting
Already handled by Next.js:
- Each route is lazy-loaded
- Components are tree-shaken
- Images are optimized

---

## 🚀 Deployment

### Vercel (Recommended - v0 built for this)
```bash
# Push to GitHub
git push origin main

# Vercel auto-deploys on push
# Set environment variables in Vercel dashboard
```

### Manual Deployment
```bash
pnpm run build
pnpm start  # Production server
```

### Environment in Production
```
NEXT_PUBLIC_API_URL = https://api.yoursite.com
```

Update API URL for production environment.

---

## 🆘 Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| "useAuth must be used within AuthProvider" | Ensure AuthProvider wraps app in layout.tsx |
| Form validation not working | Verify zodResolver is used in useForm |
| Tests not showing | Check testType is valid ('phq9', 'bdi2', etc.) |
| Styles look broken | Run `pnpm install` to ensure Tailwind installed |
| API calls failing | Check NEXT_PUBLIC_API_URL matches backend |
| Token not persisting | localStorage is being used (backend can use cookies) |

---

## 📞 Quick Help

**"How do I...?"**

| Task | Location |
|------|----------|
| Change app name | `README.md`, `app/layout.tsx`, `app/page.tsx` |
| Add a test | `lib/test-data.ts` (4 steps) |
| Modify colors | `app/globals.css` |
| Update questions | `lib/test-data.ts` |
| Change recommendations | `lib/test-data.ts` |
| Add auth method | `lib/auth-context.tsx` + backend |
| Create new page | Copy `app/auth/login/page.tsx` pattern |
| Customize styling | Check `tailwind.config.ts` + `app/globals.css` |
| Add validation | Update `lib/schemas.ts` + backend |

---

## ✨ Key Features At a Glance

✅ 4 assessment tests
✅ Immediate scoring & results  
✅ User authentication
✅ Profile management
✅ Mobile responsive
✅ Accessibility compliant
✅ Form validation (frontend + backend ready)
✅ Error handling
✅ Protected routes
✅ Semantic design tokens
✅ Comprehensive documentation
✅ Production-ready code

---

**That's it!** For more details, see the full documentation files in the project.

Happy coding! 🎉

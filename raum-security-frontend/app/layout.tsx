"use client";

import "@mantine/core/styles.css";
import "@mantine/notifications/styles.css";
import { Notifications } from "@mantine/notifications";
import {
  AppShell,
  Burger,
  ColorSchemeScript,
  MantineProvider,
  NavLink,
  Stack,
  Title,
  mantineHtmlProps,
} from "@mantine/core";
import Link from "next/link";
import { useDisclosure } from "@mantine/hooks";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [opened, { toggle }] = useDisclosure();
  return (
    <html lang="en" {...mantineHtmlProps}>
      <head>
        <ColorSchemeScript />
      </head>
      <body>
        <MantineProvider>
          <Notifications />
          <AppShell
            header={{ height: 60 }}
            navbar={{
              width: 300,
              breakpoint: "sm",
              collapsed: { mobile: !opened },
            }}
            padding="md"
          >
            <AppShell.Header>
              <Burger
                opened={opened}
                onClick={toggle}
                hiddenFrom="sm"
                size="sm"
              />
              <div>
                <Title pl="md" pt="sm">
                  Raum Security
                </Title>
              </div>
            </AppShell.Header>

            <AppShell.Navbar p="md">
              <Stack>
                <Link
                  href="/"
                  style={{ textDecoration: "none", color: "inherit" }}
                >
                  <NavLink label="List alarms" />
                </Link>
                <Link
                  href="/create-alarm"
                  style={{ textDecoration: "none", color: "inherit" }}
                >
                  <NavLink label="Create new Alarm" />
                </Link>
              </Stack>
            </AppShell.Navbar>

            <AppShell.Main>{children}</AppShell.Main>
          </AppShell>
        </MantineProvider>
      </body>
    </html>
  );
}

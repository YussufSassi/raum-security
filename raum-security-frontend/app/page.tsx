/* eslint-disable @next/next/no-async-client-component */
"use client";

import { Table, Badge, PasswordInput, Box } from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import { Alarm, api } from "@/lib/api";
import { IconAlertSquareRounded } from "@tabler/icons-react";
import { useEffect, useState } from "react";
import Link from "next/link";

export default function Home() {
  const [alarms, setAlarms] = useState<Alarm[]>([]);

  useEffect(() => {
    api.getAlarms().then((alarms) => {
      setAlarms(alarms);
    });
  }, []);

  const [visible, { toggle }] = useDisclosure(false);
  const rows = alarms.map((alarm) => (
    <Table.Tr key={alarm.name}>
      <Table.Td>
        <Link href={`/events/${alarm.id}`}>{alarm.name}</Link>
      </Table.Td>
      <Table.Td>
        <Badge
          leftSection={
            alarm.is_active ? <IconAlertSquareRounded size={16} /> : null
          }
          color={alarm.is_active ? "yellow" : "gray"}
        >
          {alarm.is_active ? "Armed" : "Inactive"}
        </Badge>
      </Table.Td>
      <Table.Td>
        <PasswordInput
          value={alarm.admin_id}
          readOnly
          visible={visible}
          onVisibilityChange={toggle}
          placeholder="Admin Password"
        />
      </Table.Td>
    </Table.Tr>
  ));

  return (
    <Box p="md">
      <Box bg="gray.1" p="md" w="25%">
        <h1>{alarms.length}</h1>
        <span>Alarms</span>
      </Box>
      <Table>
        <Table.Thead>
          <Table.Tr>
            <Table.Th>Alarm Name</Table.Th>
            <Table.Th>Alarm Status</Table.Th>
            <Table.Th>Admin Password</Table.Th>
          </Table.Tr>
        </Table.Thead>
        <Table.Tbody>{rows}</Table.Tbody>
      </Table>
    </Box>
  );
}

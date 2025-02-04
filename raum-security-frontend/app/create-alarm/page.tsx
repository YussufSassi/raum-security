"use client";
import { Alarm, api } from "@/lib/api";
import { Card, Text, Group, Button, Stack, TextInput } from "@mantine/core";
import { useEffect, useState } from "react";
import { useForm } from "@mantine/form";
import { notifications } from "@mantine/notifications";

export default function CreateAlarm() {
  const [alarms, setAlarms] = useState<Alarm[]>([]);

  const form = useForm({
    mode: "uncontrolled",
    initialValues: {
      name: "",
      admin_id: "",
    },
  });

  useEffect(() => {
    api.getAlarms().then((alarms) => setAlarms(alarms));
  }, []);

  async function createAlarm(data: Alarm) {
    return await api.createAlarm(data).then(() => {
      notifications.show({
        title: "Alarm Created",
        message: "Alarm created successfully",
      });
      setAlarms([...alarms, data]);
      form.reset();
    });
  }

  async function deleteAlarm(alarmId: number) {
    return await api.deleteAlarm(alarmId).then(() => {
      notifications.show({
        title: "Alarm Deleted",
        message: "Alarm deleted successfully",
      });
      setAlarms(alarms.filter((alarm) => alarm.id !== alarmId));
    });
  }

  return (
    <div className="m-10">
      <Stack gap="xl">
        <div>
          <h1 className="font-extrabold text-2xl mb-6">Create Alarm</h1>

          <form
            onSubmit={form.onSubmit((values) => {
              createAlarm(values);
            })}
          >
            <TextInput
              withAsterisk
              label="Alarm Name"
              placeholder="My Alarm"
              key={form.key("name")}
              {...form.getInputProps("name")}
            />

            <TextInput
              withAsterisk
              label="Admin Password"
              placeholder="1234567890"
              key={form.key("admin_id")}
              {...form.getInputProps("admin_id")}
            />

            <Group justify="flex-end" mt="md">
              <Button type="submit">Create Alarm</Button>
            </Group>
          </form>
        </div>

        <div>
          <h2 className="font-bold text-xl mb-4">Existing Alarms</h2>
          <Stack>
            {alarms.map((alarm) => (
              <Card
                key={alarm.id}
                shadow="sm"
                padding="lg"
                radius="md"
                withBorder
              >
                <Group justify="space-between" mb="xs">
                  <Text fw={500} size="lg">
                    {alarm.name}
                  </Text>
                </Group>

                <Text size="sm" c="dimmed">
                  Admin ID: {alarm.admin_id}
                </Text>

                <Button
                  color="red"
                  fullWidth
                  mt="md"
                  radius="md"
                  variant="light"
                  onClick={() => deleteAlarm(alarm.id!)}
                >
                  Delete Alarm
                </Button>
              </Card>
            ))}
          </Stack>
        </div>
      </Stack>
    </div>
  );
}

# SNMP MIB module (JUNIPER-CHASSIS-HA-RESWATCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-CHASSIS-HA-RESWATCH-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:48:42 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(jnxJsReswatchHA,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsReswatchHA")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxJsReswatchHAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1)
)
if mibBuilder.loadTexts:
    jnxJsReswatchHAMIB.setRevisions(
        ("2020-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsReswatchHANotifications_ObjectIdentity = ObjectIdentity
jnxJsReswatchHANotifications = _JnxJsReswatchHANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 0)
)
_JnxJsReswatchHATrapObjects_ObjectIdentity = ObjectIdentity
jnxJsReswatchHATrapObjects = _JnxJsReswatchHATrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1)
)
_JnxJsChHACpuBusyInfoIdlePercent_Type = DisplayString
_JnxJsChHACpuBusyInfoIdlePercent_Object = MibScalar
jnxJsChHACpuBusyInfoIdlePercent = _JnxJsChHACpuBusyInfoIdlePercent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1, 1),
    _JnxJsChHACpuBusyInfoIdlePercent_Type()
)
jnxJsChHACpuBusyInfoIdlePercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHACpuBusyInfoIdlePercent.setStatus("current")
_JnxJsChHACpuBusyInfoProc0_Type = DisplayString
_JnxJsChHACpuBusyInfoProc0_Object = MibScalar
jnxJsChHACpuBusyInfoProc0 = _JnxJsChHACpuBusyInfoProc0_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1, 2),
    _JnxJsChHACpuBusyInfoProc0_Type()
)
jnxJsChHACpuBusyInfoProc0.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHACpuBusyInfoProc0.setStatus("current")
_JnxJsChHACpuBusyInfoProc1_Type = DisplayString
_JnxJsChHACpuBusyInfoProc1_Object = MibScalar
jnxJsChHACpuBusyInfoProc1 = _JnxJsChHACpuBusyInfoProc1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1, 3),
    _JnxJsChHACpuBusyInfoProc1_Type()
)
jnxJsChHACpuBusyInfoProc1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHACpuBusyInfoProc1.setStatus("current")
_JnxJsChHACpuBusyInfoProc2_Type = DisplayString
_JnxJsChHACpuBusyInfoProc2_Object = MibScalar
jnxJsChHACpuBusyInfoProc2 = _JnxJsChHACpuBusyInfoProc2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1, 4),
    _JnxJsChHACpuBusyInfoProc2_Type()
)
jnxJsChHACpuBusyInfoProc2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHACpuBusyInfoProc2.setStatus("current")
_JnxJsChHACpuBusyInfoReason_Type = DisplayString
_JnxJsChHACpuBusyInfoReason_Object = MibScalar
jnxJsChHACpuBusyInfoReason = _JnxJsChHACpuBusyInfoReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1, 5),
    _JnxJsChHACpuBusyInfoReason_Type()
)
jnxJsChHACpuBusyInfoReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHACpuBusyInfoReason.setStatus("current")
_JnxJsChHAJklBusyInfoLoadPercent_Type = DisplayString
_JnxJsChHAJklBusyInfoLoadPercent_Object = MibScalar
jnxJsChHAJklBusyInfoLoadPercent = _JnxJsChHAJklBusyInfoLoadPercent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1, 6),
    _JnxJsChHAJklBusyInfoLoadPercent_Type()
)
jnxJsChHAJklBusyInfoLoadPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAJklBusyInfoLoadPercent.setStatus("current")
_JnxJsChHAJklBusyInfoReason_Type = DisplayString
_JnxJsChHAJklBusyInfoReason_Object = MibScalar
jnxJsChHAJklBusyInfoReason = _JnxJsChHAJklBusyInfoReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 1, 7),
    _JnxJsChHAJklBusyInfoReason_Type()
)
jnxJsChHAJklBusyInfoReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsChHAJklBusyInfoReason.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJsChHACpuBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 0, 1)
)
jnxJsChHACpuBusy.setObjects(
      *(("JUNIPER-CHASSIS-HA-RESWATCH-MIB", "jnxJsChHACpuBusyInfoIdlePercent"),
        ("JUNIPER-CHASSIS-HA-RESWATCH-MIB", "jnxJsChHACpuBusyInfoProc0"),
        ("JUNIPER-CHASSIS-HA-RESWATCH-MIB", "jnxJsChHACpuBusyInfoProc1"),
        ("JUNIPER-CHASSIS-HA-RESWATCH-MIB", "jnxJsChHACpuBusyInfoProc2"),
        ("JUNIPER-CHASSIS-HA-RESWATCH-MIB", "jnxJsChHACpuBusyInfoReason"))
)
if mibBuilder.loadTexts:
    jnxJsChHACpuBusy.setStatus(
        "current"
    )

jnxJsChHAJklBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 20, 1, 0, 2)
)
jnxJsChHAJklBusy.setObjects(
      *(("JUNIPER-CHASSIS-HA-RESWATCH-MIB", "jnxJsChHAJklBusyInfoLoadPercent"),
        ("JUNIPER-CHASSIS-HA-RESWATCH-MIB", "jnxJsChHAJklBusyInfoReason"))
)
if mibBuilder.loadTexts:
    jnxJsChHAJklBusy.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-CHASSIS-HA-RESWATCH-MIB",
    **{"jnxJsReswatchHAMIB": jnxJsReswatchHAMIB,
       "jnxJsReswatchHANotifications": jnxJsReswatchHANotifications,
       "jnxJsChHACpuBusy": jnxJsChHACpuBusy,
       "jnxJsChHAJklBusy": jnxJsChHAJklBusy,
       "jnxJsReswatchHATrapObjects": jnxJsReswatchHATrapObjects,
       "jnxJsChHACpuBusyInfoIdlePercent": jnxJsChHACpuBusyInfoIdlePercent,
       "jnxJsChHACpuBusyInfoProc0": jnxJsChHACpuBusyInfoProc0,
       "jnxJsChHACpuBusyInfoProc1": jnxJsChHACpuBusyInfoProc1,
       "jnxJsChHACpuBusyInfoProc2": jnxJsChHACpuBusyInfoProc2,
       "jnxJsChHACpuBusyInfoReason": jnxJsChHACpuBusyInfoReason,
       "jnxJsChHAJklBusyInfoLoadPercent": jnxJsChHAJklBusyInfoLoadPercent,
       "jnxJsChHAJklBusyInfoReason": jnxJsChHAJklBusyInfoReason}
)

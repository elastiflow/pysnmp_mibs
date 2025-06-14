# SNMP MIB module (RTBRICK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/rtbrick_50058/RTBRICK-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:56:02 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rtbrick = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50058)
)
if mibBuilder.loadTexts:
    rtbrick.setRevisions(
        ("2019-03-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RtbrickTables_ObjectIdentity = ObjectIdentity
rtbrickTables = _RtbrickTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 101)
)
_RtbrickProducts_ObjectIdentity = ObjectIdentity
rtbrickProducts = _RtbrickProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 102)
)
_RtbrickTraps_ObjectIdentity = ObjectIdentity
rtbrickTraps = _RtbrickTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 103)
)
_RtbrickSyslogNotifications_ObjectIdentity = ObjectIdentity
rtbrickSyslogNotifications = _RtbrickSyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 103, 1)
)
_RtbrickModules_ObjectIdentity = ObjectIdentity
rtbrickModules = _RtbrickModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50058, 104)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RTBRICK-MIB",
    **{"rtbrick": rtbrick,
       "rtbrickTables": rtbrickTables,
       "rtbrickProducts": rtbrickProducts,
       "rtbrickTraps": rtbrickTraps,
       "rtbrickSyslogNotifications": rtbrickSyslogNotifications,
       "rtbrickModules": rtbrickModules}
)

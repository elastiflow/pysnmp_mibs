# SNMP MIB module (RBN-SUBSCRIBER-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-SUBSCRIBER-SESSION-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:32 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnSubscriberSessionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10)
)
if mibBuilder.loadTexts:
    rbnSubscriberSessionMib.setRevisions(
        ("2000-09-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSubscriberSessionMibObjects_ObjectIdentity = ObjectIdentity
rbnSubscriberSessionMibObjects = _RbnSubscriberSessionMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 1)
)
_RbnSubSessionBranch_ObjectIdentity = ObjectIdentity
rbnSubSessionBranch = _RbnSubSessionBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 1, 1)
)
_RbnSubscriberSessionTable_Object = MibTable
rbnSubscriberSessionTable = _RbnSubscriberSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSubscriberSessionTable.setStatus("current")
_RbnSubscriberSessionEntry_Object = MibTableRow
rbnSubscriberSessionEntry = _RbnSubscriberSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 1, 1, 1, 1)
)
rbnSubscriberSessionEntry.setIndexNames(
    (0, "RBN-SUBSCRIBER-SESSION-MIB", "rbnSubscriberSessionId"),
)
if mibBuilder.loadTexts:
    rbnSubscriberSessionEntry.setStatus("current")
_RbnSubscriberSessionId_Type = SnmpAdminString
_RbnSubscriberSessionId_Object = MibTableColumn
rbnSubscriberSessionId = _RbnSubscriberSessionId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 1, 1, 1, 1, 1),
    _RbnSubscriberSessionId_Type()
)
rbnSubscriberSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSubscriberSessionId.setStatus("current")
_RbnSubscriberSessionActive_Type = TruthValue
_RbnSubscriberSessionActive_Object = MibTableColumn
rbnSubscriberSessionActive = _RbnSubscriberSessionActive_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 1, 1, 1, 1, 2),
    _RbnSubscriberSessionActive_Type()
)
rbnSubscriberSessionActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubscriberSessionActive.setStatus("current")
_RbnSubscriberSessionMibConformance_ObjectIdentity = ObjectIdentity
rbnSubscriberSessionMibConformance = _RbnSubscriberSessionMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 2)
)
_RbnSubSessionCompliances_ObjectIdentity = ObjectIdentity
rbnSubSessionCompliances = _RbnSubSessionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 2, 1)
)
_RbnSubSessionGroups_ObjectIdentity = ObjectIdentity
rbnSubSessionGroups = _RbnSubSessionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 2, 2)
)
_RbnSubscriberSessionMibNotifications_ObjectIdentity = ObjectIdentity
rbnSubscriberSessionMibNotifications = _RbnSubscriberSessionMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 3)
)

# Managed Objects groups

rbnSubsSessionActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 2, 2, 1)
)
rbnSubsSessionActiveGroup.setObjects(
    ("RBN-SUBSCRIBER-SESSION-MIB", "rbnSubscriberSessionActive")
)
if mibBuilder.loadTexts:
    rbnSubsSessionActiveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnSubSessionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 10, 2, 1, 1)
)
rbnSubSessionCompliance.setObjects(
    ("RBN-SUBSCRIBER-SESSION-MIB", "rbnSubsSessionActiveGroup")
)
if mibBuilder.loadTexts:
    rbnSubSessionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SUBSCRIBER-SESSION-MIB",
    **{"rbnSubscriberSessionMib": rbnSubscriberSessionMib,
       "rbnSubscriberSessionMibObjects": rbnSubscriberSessionMibObjects,
       "rbnSubSessionBranch": rbnSubSessionBranch,
       "rbnSubscriberSessionTable": rbnSubscriberSessionTable,
       "rbnSubscriberSessionEntry": rbnSubscriberSessionEntry,
       "rbnSubscriberSessionId": rbnSubscriberSessionId,
       "rbnSubscriberSessionActive": rbnSubscriberSessionActive,
       "rbnSubscriberSessionMibConformance": rbnSubscriberSessionMibConformance,
       "rbnSubSessionCompliances": rbnSubSessionCompliances,
       "rbnSubSessionCompliance": rbnSubSessionCompliance,
       "rbnSubSessionGroups": rbnSubSessionGroups,
       "rbnSubsSessionActiveGroup": rbnSubsSessionActiveGroup,
       "rbnSubscriberSessionMibNotifications": rbnSubscriberSessionMibNotifications}
)

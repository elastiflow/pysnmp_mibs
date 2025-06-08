# SNMP MIB module (RBN-SUBSCRIBER-REAUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-SUBSCRIBER-REAUTH-MIB.mib
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

(rbnSubscriberSessionEntry,) = mibBuilder.importSymbols(
    "RBN-SUBSCRIBER-SESSION-MIB",
    "rbnSubscriberSessionEntry")

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

rbnSubscriberReauthMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14)
)
if mibBuilder.loadTexts:
    rbnSubscriberReauthMib.setRevisions(
        ("2002-01-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSubscriberReauthMibObjects_ObjectIdentity = ObjectIdentity
rbnSubscriberReauthMibObjects = _RbnSubscriberReauthMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 1)
)
_RbnSubscriberReauthName_Type = SnmpAdminString
_RbnSubscriberReauthName_Object = MibScalar
rbnSubscriberReauthName = _RbnSubscriberReauthName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 1, 1),
    _RbnSubscriberReauthName_Type()
)
rbnSubscriberReauthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubscriberReauthName.setStatus("current")
_RbnSubscriberReauthTable_Object = MibTable
rbnSubscriberReauthTable = _RbnSubscriberReauthTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    rbnSubscriberReauthTable.setStatus("current")
_RbnSubscriberReauthEntry_Object = MibTableRow
rbnSubscriberReauthEntry = _RbnSubscriberReauthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbnSubscriberReauthEntry.setStatus("current")
_RbnSubscriberReauthNow_Type = TruthValue
_RbnSubscriberReauthNow_Object = MibTableColumn
rbnSubscriberReauthNow = _RbnSubscriberReauthNow_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 1, 2, 1, 1),
    _RbnSubscriberReauthNow_Type()
)
rbnSubscriberReauthNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSubscriberReauthNow.setStatus("current")
_RbnSubscriberReauthMibConformance_ObjectIdentity = ObjectIdentity
rbnSubscriberReauthMibConformance = _RbnSubscriberReauthMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 2)
)
_RbnSubReauthCompliances_ObjectIdentity = ObjectIdentity
rbnSubReauthCompliances = _RbnSubReauthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 2, 1)
)
_RbnSubReauthGroups_ObjectIdentity = ObjectIdentity
rbnSubReauthGroups = _RbnSubReauthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 2, 2)
)
_RbnSubscriberReauthMibNotifications_ObjectIdentity = ObjectIdentity
rbnSubscriberReauthMibNotifications = _RbnSubscriberReauthMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 3)
)
rbnSubscriberSessionEntry.registerAugmentions(
    ("RBN-SUBSCRIBER-REAUTH-MIB",
     "rbnSubscriberReauthEntry")
)
rbnSubscriberReauthEntry.setIndexNames(*rbnSubscriberSessionEntry.getIndexNames())

# Managed Objects groups

rbnSubscriberReauthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 2, 2, 1)
)
rbnSubscriberReauthGroup.setObjects(
      *(("RBN-SUBSCRIBER-REAUTH-MIB", "rbnSubscriberReauthName"),
        ("RBN-SUBSCRIBER-REAUTH-MIB", "rbnSubscriberReauthNow"))
)
if mibBuilder.loadTexts:
    rbnSubscriberReauthGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnSubReauthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 14, 2, 1, 1)
)
rbnSubReauthCompliance.setObjects(
    ("RBN-SUBSCRIBER-REAUTH-MIB", "rbnSubscriberReauthGroup")
)
if mibBuilder.loadTexts:
    rbnSubReauthCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SUBSCRIBER-REAUTH-MIB",
    **{"rbnSubscriberReauthMib": rbnSubscriberReauthMib,
       "rbnSubscriberReauthMibObjects": rbnSubscriberReauthMibObjects,
       "rbnSubscriberReauthName": rbnSubscriberReauthName,
       "rbnSubscriberReauthTable": rbnSubscriberReauthTable,
       "rbnSubscriberReauthEntry": rbnSubscriberReauthEntry,
       "rbnSubscriberReauthNow": rbnSubscriberReauthNow,
       "rbnSubscriberReauthMibConformance": rbnSubscriberReauthMibConformance,
       "rbnSubReauthCompliances": rbnSubReauthCompliances,
       "rbnSubReauthCompliance": rbnSubReauthCompliance,
       "rbnSubReauthGroups": rbnSubReauthGroups,
       "rbnSubscriberReauthGroup": rbnSubscriberReauthGroup,
       "rbnSubscriberReauthMibNotifications": rbnSubscriberReauthMibNotifications}
)

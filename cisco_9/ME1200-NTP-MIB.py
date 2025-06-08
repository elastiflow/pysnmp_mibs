# SNMP MIB module (ME1200-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-NTP-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200InetAddress,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InetAddress")

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

me1200NtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57)
)
if mibBuilder.loadTexts:
    me1200NtpMib.setRevisions(
        ("2014-05-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Me1200NtpMibObjects_ObjectIdentity = ObjectIdentity
me1200NtpMibObjects = _Me1200NtpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1)
)
_Me1200NtpConfig_ObjectIdentity = ObjectIdentity
me1200NtpConfig = _Me1200NtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2)
)
_Me1200NtpConfigGlobals_ObjectIdentity = ObjectIdentity
me1200NtpConfigGlobals = _Me1200NtpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 1)
)
_Me1200NtpConfigGlobalsMode_Type = TruthValue
_Me1200NtpConfigGlobalsMode_Object = MibScalar
me1200NtpConfigGlobalsMode = _Me1200NtpConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 1, 1),
    _Me1200NtpConfigGlobalsMode_Type()
)
me1200NtpConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200NtpConfigGlobalsMode.setStatus("current")
_Me1200NtpConfigServerTable_Object = MibTable
me1200NtpConfigServerTable = _Me1200NtpConfigServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200NtpConfigServerTable.setStatus("current")
_Me1200NtpConfigServerEntry_Object = MibTableRow
me1200NtpConfigServerEntry = _Me1200NtpConfigServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2, 1)
)
me1200NtpConfigServerEntry.setIndexNames(
    (0, "ME1200-NTP-MIB", "me1200NtpConfigServerIndex"),
)
if mibBuilder.loadTexts:
    me1200NtpConfigServerEntry.setStatus("current")


class _Me1200NtpConfigServerIndex_Type(Integer32):
    """Custom type me1200NtpConfigServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Me1200NtpConfigServerIndex_Type.__name__ = "Integer32"
_Me1200NtpConfigServerIndex_Object = MibTableColumn
me1200NtpConfigServerIndex = _Me1200NtpConfigServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2, 1, 1),
    _Me1200NtpConfigServerIndex_Type()
)
me1200NtpConfigServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200NtpConfigServerIndex.setStatus("current")
_Me1200NtpConfigServerAddress_Type = ME1200InetAddress
_Me1200NtpConfigServerAddress_Object = MibTableColumn
me1200NtpConfigServerAddress = _Me1200NtpConfigServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 1, 2, 2, 1, 2),
    _Me1200NtpConfigServerAddress_Type()
)
me1200NtpConfigServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200NtpConfigServerAddress.setStatus("current")
_Me1200NtpMibConformance_ObjectIdentity = ObjectIdentity
me1200NtpMibConformance = _Me1200NtpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2)
)
_Me1200NtpMibCompliances_ObjectIdentity = ObjectIdentity
me1200NtpMibCompliances = _Me1200NtpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 1)
)
_Me1200NtpMibGroups_ObjectIdentity = ObjectIdentity
me1200NtpMibGroups = _Me1200NtpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 2)
)

# Managed Objects groups

me1200NtpConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 2, 1)
)
me1200NtpConfigGlobalsInfoGroup.setObjects(
    ("ME1200-NTP-MIB", "me1200NtpConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    me1200NtpConfigGlobalsInfoGroup.setStatus("current")

me1200NtpConfigServerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 2, 2)
)
me1200NtpConfigServerTableInfoGroup.setObjects(
    ("ME1200-NTP-MIB", "me1200NtpConfigServerAddress")
)
if mibBuilder.loadTexts:
    me1200NtpConfigServerTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200NtpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 57, 2, 1, 1)
)
me1200NtpMibCompliance.setObjects(
      *(("ME1200-NTP-MIB", "me1200NtpConfigGlobalsInfoGroup"),
        ("ME1200-NTP-MIB", "me1200NtpConfigServerTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200NtpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-NTP-MIB",
    **{"me1200NtpMib": me1200NtpMib,
       "me1200NtpMibObjects": me1200NtpMibObjects,
       "me1200NtpConfig": me1200NtpConfig,
       "me1200NtpConfigGlobals": me1200NtpConfigGlobals,
       "me1200NtpConfigGlobalsMode": me1200NtpConfigGlobalsMode,
       "me1200NtpConfigServerTable": me1200NtpConfigServerTable,
       "me1200NtpConfigServerEntry": me1200NtpConfigServerEntry,
       "me1200NtpConfigServerIndex": me1200NtpConfigServerIndex,
       "me1200NtpConfigServerAddress": me1200NtpConfigServerAddress,
       "me1200NtpMibConformance": me1200NtpMibConformance,
       "me1200NtpMibCompliances": me1200NtpMibCompliances,
       "me1200NtpMibCompliance": me1200NtpMibCompliance,
       "me1200NtpMibGroups": me1200NtpMibGroups,
       "me1200NtpConfigGlobalsInfoGroup": me1200NtpConfigGlobalsInfoGroup,
       "me1200NtpConfigServerTableInfoGroup": me1200NtpConfigServerTableInfoGroup}
)

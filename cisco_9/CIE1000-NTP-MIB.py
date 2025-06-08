# SNMP MIB module (CIE1000-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-NTP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000InetAddress,) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000InetAddress")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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

cie1000NtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57)
)
if mibBuilder.loadTexts:
    cie1000NtpMib.setRevisions(
        ("2014-10-10 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cie1000NtpMibObjects_ObjectIdentity = ObjectIdentity
cie1000NtpMibObjects = _Cie1000NtpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1)
)
_Cie1000NtpConfig_ObjectIdentity = ObjectIdentity
cie1000NtpConfig = _Cie1000NtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2)
)
_Cie1000NtpConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000NtpConfigGlobals = _Cie1000NtpConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 1)
)
_Cie1000NtpConfigGlobalsMode_Type = TruthValue
_Cie1000NtpConfigGlobalsMode_Object = MibScalar
cie1000NtpConfigGlobalsMode = _Cie1000NtpConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 1, 1),
    _Cie1000NtpConfigGlobalsMode_Type()
)
cie1000NtpConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000NtpConfigGlobalsMode.setStatus("current")
_Cie1000NtpConfigServerTable_Object = MibTable
cie1000NtpConfigServerTable = _Cie1000NtpConfigServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000NtpConfigServerTable.setStatus("current")
_Cie1000NtpConfigServerEntry_Object = MibTableRow
cie1000NtpConfigServerEntry = _Cie1000NtpConfigServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2, 1)
)
cie1000NtpConfigServerEntry.setIndexNames(
    (0, "CIE1000-NTP-MIB", "cie1000NtpConfigServerIndex"),
)
if mibBuilder.loadTexts:
    cie1000NtpConfigServerEntry.setStatus("current")


class _Cie1000NtpConfigServerIndex_Type(Integer32):
    """Custom type cie1000NtpConfigServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Cie1000NtpConfigServerIndex_Type.__name__ = "Integer32"
_Cie1000NtpConfigServerIndex_Object = MibTableColumn
cie1000NtpConfigServerIndex = _Cie1000NtpConfigServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2, 1, 1),
    _Cie1000NtpConfigServerIndex_Type()
)
cie1000NtpConfigServerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000NtpConfigServerIndex.setStatus("current")
_Cie1000NtpConfigServerAddress_Type = CIE1000InetAddress
_Cie1000NtpConfigServerAddress_Object = MibTableColumn
cie1000NtpConfigServerAddress = _Cie1000NtpConfigServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 1, 2, 2, 1, 2),
    _Cie1000NtpConfigServerAddress_Type()
)
cie1000NtpConfigServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000NtpConfigServerAddress.setStatus("current")
_Cie1000NtpMibConformance_ObjectIdentity = ObjectIdentity
cie1000NtpMibConformance = _Cie1000NtpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2)
)
_Cie1000NtpMibCompliances_ObjectIdentity = ObjectIdentity
cie1000NtpMibCompliances = _Cie1000NtpMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 1)
)
_Cie1000NtpMibGroups_ObjectIdentity = ObjectIdentity
cie1000NtpMibGroups = _Cie1000NtpMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 2)
)

# Managed Objects groups

cie1000NtpConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 2, 1)
)
cie1000NtpConfigGlobalsInfoGroup.setObjects(
    ("CIE1000-NTP-MIB", "cie1000NtpConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    cie1000NtpConfigGlobalsInfoGroup.setStatus("current")

cie1000NtpConfigServerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 2, 2)
)
cie1000NtpConfigServerTableInfoGroup.setObjects(
      *(("CIE1000-NTP-MIB", "cie1000NtpConfigServerIndex"),
        ("CIE1000-NTP-MIB", "cie1000NtpConfigServerAddress"))
)
if mibBuilder.loadTexts:
    cie1000NtpConfigServerTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000NtpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 57, 2, 1, 1)
)
cie1000NtpMibCompliance.setObjects(
      *(("CIE1000-NTP-MIB", "cie1000NtpConfigGlobalsInfoGroup"),
        ("CIE1000-NTP-MIB", "cie1000NtpConfigServerTableInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000NtpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-NTP-MIB",
    **{"cie1000NtpMib": cie1000NtpMib,
       "cie1000NtpMibObjects": cie1000NtpMibObjects,
       "cie1000NtpConfig": cie1000NtpConfig,
       "cie1000NtpConfigGlobals": cie1000NtpConfigGlobals,
       "cie1000NtpConfigGlobalsMode": cie1000NtpConfigGlobalsMode,
       "cie1000NtpConfigServerTable": cie1000NtpConfigServerTable,
       "cie1000NtpConfigServerEntry": cie1000NtpConfigServerEntry,
       "cie1000NtpConfigServerIndex": cie1000NtpConfigServerIndex,
       "cie1000NtpConfigServerAddress": cie1000NtpConfigServerAddress,
       "cie1000NtpMibConformance": cie1000NtpMibConformance,
       "cie1000NtpMibCompliances": cie1000NtpMibCompliances,
       "cie1000NtpMibCompliance": cie1000NtpMibCompliance,
       "cie1000NtpMibGroups": cie1000NtpMibGroups,
       "cie1000NtpConfigGlobalsInfoGroup": cie1000NtpConfigGlobalsInfoGroup,
       "cie1000NtpConfigServerTableInfoGroup": cie1000NtpConfigServerTableInfoGroup}
)

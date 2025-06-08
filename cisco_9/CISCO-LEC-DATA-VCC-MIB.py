# SNMP MIB module (CISCO-LEC-DATA-VCC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LEC-DATA-VCC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:33 2025
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(AtmLaneAddress,
 lecIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress",
    "lecIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ciscoLecDataVccMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69)
)
if mibBuilder.loadTexts:
    ciscoLecDataVccMIB.setRevisions(
        ("1997-01-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLecDataVccMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLecDataVccMIBObjects = _CiscoLecDataVccMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 1)
)
_CLecDataDirectVcc_ObjectIdentity = ObjectIdentity
cLecDataDirectVcc = _CLecDataDirectVcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1)
)
_CLecDataDirectVccTable_Object = MibTable
cLecDataDirectVccTable = _CLecDataDirectVccTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLecDataDirectVccTable.setStatus("current")
_CLecDataDirectVccEntry_Object = MibTableRow
cLecDataDirectVccEntry = _CLecDataDirectVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1)
)
cLecDataDirectVccEntry.setIndexNames(
    (0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"),
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    cLecDataDirectVccEntry.setStatus("current")
_CLecDataDirectLocalAtmAddress_Type = AtmLaneAddress
_CLecDataDirectLocalAtmAddress_Object = MibTableColumn
cLecDataDirectLocalAtmAddress = _CLecDataDirectLocalAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 1),
    _CLecDataDirectLocalAtmAddress_Type()
)
cLecDataDirectLocalAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLecDataDirectLocalAtmAddress.setStatus("current")
_CLecDataDirectRemoteAtmAddress_Type = AtmLaneAddress
_CLecDataDirectRemoteAtmAddress_Object = MibTableColumn
cLecDataDirectRemoteAtmAddress = _CLecDataDirectRemoteAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 2),
    _CLecDataDirectRemoteAtmAddress_Type()
)
cLecDataDirectRemoteAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLecDataDirectRemoteAtmAddress.setStatus("current")
_CiscoLecDataVccMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoLecDataVccMIBNotificationPrefix = _CiscoLecDataVccMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 2)
)
_CiscoLecDataVccMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoLecDataVccMIBNotifications = _CiscoLecDataVccMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 2, 0)
)
_CiscoLecDataVccMIBConformance_ObjectIdentity = ObjectIdentity
ciscoLecDataVccMIBConformance = _CiscoLecDataVccMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 3)
)
_CiscoLecDataVccMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLecDataVccMIBCompliances = _CiscoLecDataVccMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1)
)
_CiscoLecDataVccMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLecDataVccMIBGroups = _CiscoLecDataVccMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2)
)

# Managed Objects groups

ciscoLecDataVccBaseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2, 1)
)
ciscoLecDataVccBaseMIBGroup.setObjects(
      *(("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectLocalAtmAddress"),
        ("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectRemoteAtmAddress"))
)
if mibBuilder.loadTexts:
    ciscoLecDataVccBaseMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLecDataVccMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1, 1)
)
ciscoLecDataVccMIBCompliance.setObjects(
    ("CISCO-LEC-DATA-VCC-MIB", "ciscoLecDataVccBaseMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoLecDataVccMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LEC-DATA-VCC-MIB",
    **{"ciscoLecDataVccMIB": ciscoLecDataVccMIB,
       "ciscoLecDataVccMIBObjects": ciscoLecDataVccMIBObjects,
       "cLecDataDirectVcc": cLecDataDirectVcc,
       "cLecDataDirectVccTable": cLecDataDirectVccTable,
       "cLecDataDirectVccEntry": cLecDataDirectVccEntry,
       "cLecDataDirectLocalAtmAddress": cLecDataDirectLocalAtmAddress,
       "cLecDataDirectRemoteAtmAddress": cLecDataDirectRemoteAtmAddress,
       "ciscoLecDataVccMIBNotificationPrefix": ciscoLecDataVccMIBNotificationPrefix,
       "ciscoLecDataVccMIBNotifications": ciscoLecDataVccMIBNotifications,
       "ciscoLecDataVccMIBConformance": ciscoLecDataVccMIBConformance,
       "ciscoLecDataVccMIBCompliances": ciscoLecDataVccMIBCompliances,
       "ciscoLecDataVccMIBCompliance": ciscoLecDataVccMIBCompliance,
       "ciscoLecDataVccMIBGroups": ciscoLecDataVccMIBGroups,
       "ciscoLecDataVccBaseMIBGroup": ciscoLecDataVccBaseMIBGroup}
)

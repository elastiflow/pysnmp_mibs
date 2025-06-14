# SNMP MIB module (CISCO-ATM-SWITCH-ADDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ATM-SWITCH-ADDR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:07:31 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAtmSwAddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 51)
)
if mibBuilder.loadTexts:
    ciscoAtmSwAddrMIB.setRevisions(
        ("1996-01-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmSwAddrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmSwAddrMIBObjects = _CiscoAtmSwAddrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 1)
)
_CiscoAtmSwAddrTable_Object = MibTable
ciscoAtmSwAddrTable = _CiscoAtmSwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSwAddrTable.setStatus("current")
_CiscoAtmSwAddrEntry_Object = MibTableRow
ciscoAtmSwAddrEntry = _CiscoAtmSwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1)
)
ciscoAtmSwAddrEntry.setIndexNames(
    (0, "CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrIndex"),
)
if mibBuilder.loadTexts:
    ciscoAtmSwAddrEntry.setStatus("current")


class _CiscoAtmSwAddrIndex_Type(Integer32):
    """Custom type ciscoAtmSwAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiscoAtmSwAddrIndex_Type.__name__ = "Integer32"
_CiscoAtmSwAddrIndex_Object = MibTableColumn
ciscoAtmSwAddrIndex = _CiscoAtmSwAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 1),
    _CiscoAtmSwAddrIndex_Type()
)
ciscoAtmSwAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmSwAddrIndex.setStatus("current")
_CiscoAtmSwAddrAddress_Type = AtmAddr
_CiscoAtmSwAddrAddress_Object = MibTableColumn
ciscoAtmSwAddrAddress = _CiscoAtmSwAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 2),
    _CiscoAtmSwAddrAddress_Type()
)
ciscoAtmSwAddrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSwAddrAddress.setStatus("current")
_CiscoAtmSwAddrRowStatus_Type = RowStatus
_CiscoAtmSwAddrRowStatus_Object = MibTableColumn
ciscoAtmSwAddrRowStatus = _CiscoAtmSwAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 3),
    _CiscoAtmSwAddrRowStatus_Type()
)
ciscoAtmSwAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoAtmSwAddrRowStatus.setStatus("current")
_CiscoAtmSwAddrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmSwAddrMIBConformance = _CiscoAtmSwAddrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 3)
)
_CiscoAtmSwAddrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmSwAddrMIBCompliances = _CiscoAtmSwAddrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1)
)
_CiscoAtmSwAddrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmSwAddrMIBGroups = _CiscoAtmSwAddrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2)
)

# Managed Objects groups

ciscoAtmSwAddrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2, 1)
)
ciscoAtmSwAddrMIBGroup.setObjects(
      *(("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrAddress"),
        ("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoAtmSwAddrMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmSwAddrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmSwAddrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-SWITCH-ADDR-MIB",
    **{"AtmAddr": AtmAddr,
       "ciscoAtmSwAddrMIB": ciscoAtmSwAddrMIB,
       "ciscoAtmSwAddrMIBObjects": ciscoAtmSwAddrMIBObjects,
       "ciscoAtmSwAddrTable": ciscoAtmSwAddrTable,
       "ciscoAtmSwAddrEntry": ciscoAtmSwAddrEntry,
       "ciscoAtmSwAddrIndex": ciscoAtmSwAddrIndex,
       "ciscoAtmSwAddrAddress": ciscoAtmSwAddrAddress,
       "ciscoAtmSwAddrRowStatus": ciscoAtmSwAddrRowStatus,
       "ciscoAtmSwAddrMIBConformance": ciscoAtmSwAddrMIBConformance,
       "ciscoAtmSwAddrMIBCompliances": ciscoAtmSwAddrMIBCompliances,
       "ciscoAtmSwAddrMIBCompliance": ciscoAtmSwAddrMIBCompliance,
       "ciscoAtmSwAddrMIBGroups": ciscoAtmSwAddrMIBGroups,
       "ciscoAtmSwAddrMIBGroup": ciscoAtmSwAddrMIBGroup}
)

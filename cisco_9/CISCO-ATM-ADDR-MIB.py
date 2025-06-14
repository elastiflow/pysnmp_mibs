# SNMP MIB module (CISCO-ATM-ADDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ATM-ADDR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:07:30 2025
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoAtmAddrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 12)
)
if mibBuilder.loadTexts:
    ciscoAtmAddrMIB.setRevisions(
        ("1996-05-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmAddr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(20, 20),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAtmAddrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmAddrMIBObjects = _CiscoAtmAddrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 1)
)
_CiscoAtmIfAdminAddrTable_Object = MibTable
ciscoAtmIfAdminAddrTable = _CiscoAtmIfAdminAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAtmIfAdminAddrTable.setStatus("current")
_CiscoAtmIfAdminAddrEntry_Object = MibTableRow
ciscoAtmIfAdminAddrEntry = _CiscoAtmIfAdminAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1)
)
ciscoAtmIfAdminAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrAddress"),
)
if mibBuilder.loadTexts:
    ciscoAtmIfAdminAddrEntry.setStatus("current")
_CiscoAtmIfAdminAddrAddress_Type = AtmAddr
_CiscoAtmIfAdminAddrAddress_Object = MibTableColumn
ciscoAtmIfAdminAddrAddress = _CiscoAtmIfAdminAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 1),
    _CiscoAtmIfAdminAddrAddress_Type()
)
ciscoAtmIfAdminAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmIfAdminAddrAddress.setStatus("current")
_CiscoAtmIfAdminAddrRowStatus_Type = RowStatus
_CiscoAtmIfAdminAddrRowStatus_Object = MibTableColumn
ciscoAtmIfAdminAddrRowStatus = _CiscoAtmIfAdminAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 1, 1, 1, 2),
    _CiscoAtmIfAdminAddrRowStatus_Type()
)
ciscoAtmIfAdminAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmIfAdminAddrRowStatus.setStatus("current")
_CiscoAtmIfAdminAddrMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmIfAdminAddrMIBConformance = _CiscoAtmIfAdminAddrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 3)
)
_CiscoAtmIfAdminAddrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmIfAdminAddrMIBCompliances = _CiscoAtmIfAdminAddrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1)
)
_CiscoAtmIfAdminAddrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmIfAdminAddrMIBGroups = _CiscoAtmIfAdminAddrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2)
)

# Managed Objects groups

ciscoAtmIfAdminAddrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 2, 1)
)
ciscoAtmIfAdminAddrMIBGroup.setObjects(
    ("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrRowStatus")
)
if mibBuilder.loadTexts:
    ciscoAtmIfAdminAddrMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoAtmIfAdminAddrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 12, 3, 1, 1)
)
ciscoAtmIfAdminAddrMIBCompliance.setObjects(
    ("CISCO-ATM-ADDR-MIB", "ciscoAtmIfAdminAddrMIBGroup")
)
if mibBuilder.loadTexts:
    ciscoAtmIfAdminAddrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-ADDR-MIB",
    **{"AtmAddr": AtmAddr,
       "ciscoAtmAddrMIB": ciscoAtmAddrMIB,
       "ciscoAtmAddrMIBObjects": ciscoAtmAddrMIBObjects,
       "ciscoAtmIfAdminAddrTable": ciscoAtmIfAdminAddrTable,
       "ciscoAtmIfAdminAddrEntry": ciscoAtmIfAdminAddrEntry,
       "ciscoAtmIfAdminAddrAddress": ciscoAtmIfAdminAddrAddress,
       "ciscoAtmIfAdminAddrRowStatus": ciscoAtmIfAdminAddrRowStatus,
       "ciscoAtmIfAdminAddrMIBConformance": ciscoAtmIfAdminAddrMIBConformance,
       "ciscoAtmIfAdminAddrMIBCompliances": ciscoAtmIfAdminAddrMIBCompliances,
       "ciscoAtmIfAdminAddrMIBCompliance": ciscoAtmIfAdminAddrMIBCompliance,
       "ciscoAtmIfAdminAddrMIBGroups": ciscoAtmIfAdminAddrMIBGroups,
       "ciscoAtmIfAdminAddrMIBGroup": ciscoAtmIfAdminAddrMIBGroup}
)

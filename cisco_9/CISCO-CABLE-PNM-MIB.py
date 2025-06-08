# SNMP MIB module (CISCO-CABLE-PNM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CABLE-PNM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:43:27 2025
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

(docsPnmCmtsUtscCfgIndex,) = mibBuilder.importSymbols(
    "DOCS-PNM-MIB",
    "docsPnmCmtsUtscCfgIndex")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCablePNMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCablePNMMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCablePNMMIBObjects = _CiscoCablePNMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1)
)
_PnmSessionObjects_ObjectIdentity = ObjectIdentity
pnmSessionObjects = _PnmSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 1)
)
_PnmSessionTable_Object = MibTable
pnmSessionTable = _PnmSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pnmSessionTable.setStatus("current")
_PnmSessionEntry_Object = MibTableRow
pnmSessionEntry = _PnmSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 1, 1, 1)
)
pnmSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-PNM-MIB", "docsPnmCmtsUtscCfgIndex"),
)
if mibBuilder.loadTexts:
    pnmSessionEntry.setStatus("current")
_PnmSessionId_Type = Unsigned32
_PnmSessionId_Object = MibTableColumn
pnmSessionId = _PnmSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 1, 1, 1, 1),
    _PnmSessionId_Type()
)
pnmSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnmSessionId.setStatus("current")
_PnmSessionSacIndex_Type = Unsigned32
_PnmSessionSacIndex_Object = MibTableColumn
pnmSessionSacIndex = _PnmSessionSacIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 1, 1, 1, 2),
    _PnmSessionSacIndex_Type()
)
pnmSessionSacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnmSessionSacIndex.setStatus("current")
_PnmSessionCreateTime_Type = DateAndTime
_PnmSessionCreateTime_Object = MibTableColumn
pnmSessionCreateTime = _PnmSessionCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 115, 1, 1, 1, 1, 3),
    _PnmSessionCreateTime_Type()
)
pnmSessionCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnmSessionCreateTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-PNM-MIB",
    **{"ciscoCablePNMMIB": ciscoCablePNMMIB,
       "ciscoCablePNMMIBObjects": ciscoCablePNMMIBObjects,
       "pnmSessionObjects": pnmSessionObjects,
       "pnmSessionTable": pnmSessionTable,
       "pnmSessionEntry": pnmSessionEntry,
       "pnmSessionId": pnmSessionId,
       "pnmSessionSacIndex": pnmSessionSacIndex,
       "pnmSessionCreateTime": pnmSessionCreateTime}
)

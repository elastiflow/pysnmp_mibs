# SNMP MIB module (CEM-IP-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-IP-IF-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

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

cemIpIfModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 24)
)
if mibBuilder.loadTexts:
    cemIpIfModule.setRevisions(
        ("2002-04-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CemIpIfForwardingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("on", 1),
          ("off", 2),
          ("network", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CemIpIfMIB_ObjectIdentity = ObjectIdentity
cemIpIfMIB = _CemIpIfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1)
)
if mibBuilder.loadTexts:
    cemIpIfMIB.setStatus("current")
_CemIpIfTables_ObjectIdentity = ObjectIdentity
cemIpIfTables = _CemIpIfTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1)
)
if mibBuilder.loadTexts:
    cemIpIfTables.setStatus("current")
_CemIpIfTable_Object = MibTable
cemIpIfTable = _CemIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cemIpIfTable.setStatus("current")
_CemIpIfEntry_Object = MibTableRow
cemIpIfEntry = _CemIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 1, 1)
)
cemIpIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cemIpIfEntry.setStatus("current")


class _CemIpIfMtu_Type(Integer32):
    """Custom type cemIpIfMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9188),
    )


_CemIpIfMtu_Type.__name__ = "Integer32"
_CemIpIfMtu_Object = MibTableColumn
cemIpIfMtu = _CemIpIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 1, 1, 1),
    _CemIpIfMtu_Type()
)
cemIpIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cemIpIfMtu.setStatus("current")


class _CemIpIfForwarding_Type(CemIpIfForwardingType):
    """Custom type cemIpIfForwarding based on CemIpIfForwardingType"""
    defaultValue = 2


_CemIpIfForwarding_Type.__name__ = "CemIpIfForwardingType"
_CemIpIfForwarding_Object = MibTableColumn
cemIpIfForwarding = _CemIpIfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 1, 1, 2),
    _CemIpIfForwarding_Type()
)
cemIpIfForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cemIpIfForwarding.setStatus("current")
_CemIpAddrCnfgTable_Object = MibTable
cemIpAddrCnfgTable = _CemIpAddrCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cemIpAddrCnfgTable.setStatus("current")
_CemIpAddrCnfgEntry_Object = MibTableRow
cemIpAddrCnfgEntry = _CemIpAddrCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 2, 1)
)
cemIpAddrCnfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CEM-IP-IF-MIB", "cemIpAddrCnfgAddress"),
)
if mibBuilder.loadTexts:
    cemIpAddrCnfgEntry.setStatus("current")
_CemIpAddrCnfgAddress_Type = IpAddress
_CemIpAddrCnfgAddress_Object = MibTableColumn
cemIpAddrCnfgAddress = _CemIpAddrCnfgAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 2, 1, 1),
    _CemIpAddrCnfgAddress_Type()
)
cemIpAddrCnfgAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cemIpAddrCnfgAddress.setStatus("current")
_CemIpAddrCnfgMask_Type = IpAddress
_CemIpAddrCnfgMask_Object = MibTableColumn
cemIpAddrCnfgMask = _CemIpAddrCnfgMask_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 2, 1, 2),
    _CemIpAddrCnfgMask_Type()
)
cemIpAddrCnfgMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemIpAddrCnfgMask.setStatus("current")
_CemIpAddrCnfgRowStatus_Type = RowStatus
_CemIpAddrCnfgRowStatus_Object = MibTableColumn
cemIpAddrCnfgRowStatus = _CemIpAddrCnfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 1, 2, 1, 3),
    _CemIpAddrCnfgRowStatus_Type()
)
cemIpAddrCnfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemIpAddrCnfgRowStatus.setStatus("current")
_CemIpIfGroups_ObjectIdentity = ObjectIdentity
cemIpIfGroups = _CemIpIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 2)
)
if mibBuilder.loadTexts:
    cemIpIfGroups.setStatus("current")
_CemIpIfConformance_ObjectIdentity = ObjectIdentity
cemIpIfConformance = _CemIpIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 3)
)
if mibBuilder.loadTexts:
    cemIpIfConformance.setStatus("current")

# Managed Objects groups

cemIpIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 2, 1)
)
cemIpIfGroup.setObjects(
      *(("CEM-IP-IF-MIB", "cemIpIfMtu"),
        ("CEM-IP-IF-MIB", "cemIpIfForwarding"))
)
if mibBuilder.loadTexts:
    cemIpIfGroup.setStatus("current")

cemIpAddrCnfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 2, 2)
)
cemIpAddrCnfgGroup.setObjects(
      *(("CEM-IP-IF-MIB", "cemIpAddrCnfgMask"),
        ("CEM-IP-IF-MIB", "cemIpAddrCnfgRowStatus"))
)
if mibBuilder.loadTexts:
    cemIpAddrCnfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cemIpIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 24, 1, 3, 1)
)
cemIpIfCompliance.setObjects(
      *(("CEM-IP-IF-MIB", "cemIpIfGroup"),
        ("CEM-IP-IF-MIB", "cemIpAddrCnfgGroup"))
)
if mibBuilder.loadTexts:
    cemIpIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-IP-IF-MIB",
    **{"CemIpIfForwardingType": CemIpIfForwardingType,
       "cemIpIfModule": cemIpIfModule,
       "cemIpIfMIB": cemIpIfMIB,
       "cemIpIfTables": cemIpIfTables,
       "cemIpIfTable": cemIpIfTable,
       "cemIpIfEntry": cemIpIfEntry,
       "cemIpIfMtu": cemIpIfMtu,
       "cemIpIfForwarding": cemIpIfForwarding,
       "cemIpAddrCnfgTable": cemIpAddrCnfgTable,
       "cemIpAddrCnfgEntry": cemIpAddrCnfgEntry,
       "cemIpAddrCnfgAddress": cemIpAddrCnfgAddress,
       "cemIpAddrCnfgMask": cemIpAddrCnfgMask,
       "cemIpAddrCnfgRowStatus": cemIpAddrCnfgRowStatus,
       "cemIpIfGroups": cemIpIfGroups,
       "cemIpIfGroup": cemIpIfGroup,
       "cemIpAddrCnfgGroup": cemIpAddrCnfgGroup,
       "cemIpIfConformance": cemIpIfConformance,
       "cemIpIfCompliance": cemIpIfCompliance}
)

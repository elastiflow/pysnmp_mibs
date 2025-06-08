# SNMP MIB module (A3COM-HUAWEI-LswSMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-LswSMON-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:03:59 2025
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

(huaweiDatacomm,
 huaweiMgmt) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiDatacomm",
    "huaweiMgmt")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSmonExtend_ObjectIdentity = ObjectIdentity
hwSmonExtend = _HwSmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26)
)
_SmonExtendObject_ObjectIdentity = ObjectIdentity
smonExtendObject = _SmonExtendObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1)
)
_Hwdot1qVlanStatNumber_Type = Integer32
_Hwdot1qVlanStatNumber_Object = MibScalar
hwdot1qVlanStatNumber = _Hwdot1qVlanStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 1),
    _Hwdot1qVlanStatNumber_Type()
)
hwdot1qVlanStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanStatNumber.setStatus("mandatory")
_Hwdot1qVlanStatStatusTable_Object = MibTable
hwdot1qVlanStatStatusTable = _Hwdot1qVlanStatStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2)
)
if mibBuilder.loadTexts:
    hwdot1qVlanStatStatusTable.setStatus("mandatory")
_Hwdot1qVlanStatStatusEntry_Object = MibTableRow
hwdot1qVlanStatStatusEntry = _Hwdot1qVlanStatStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1)
)
hwdot1qVlanStatStatusEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswSMON-MIB", "hwdot1qVlanStatEnableIndex"),
)
if mibBuilder.loadTexts:
    hwdot1qVlanStatStatusEntry.setStatus("mandatory")
_Hwdot1qVlanStatEnableIndex_Type = Integer32
_Hwdot1qVlanStatEnableIndex_Object = MibTableColumn
hwdot1qVlanStatEnableIndex = _Hwdot1qVlanStatEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1, 1),
    _Hwdot1qVlanStatEnableIndex_Type()
)
hwdot1qVlanStatEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwdot1qVlanStatEnableIndex.setStatus("mandatory")


class _Hwdot1qVlanStatEnableStatus_Type(Integer32):
    """Custom type hwdot1qVlanStatEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Hwdot1qVlanStatEnableStatus_Type.__name__ = "Integer32"
_Hwdot1qVlanStatEnableStatus_Object = MibTableColumn
hwdot1qVlanStatEnableStatus = _Hwdot1qVlanStatEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 26, 1, 2, 1, 2),
    _Hwdot1qVlanStatEnableStatus_Type()
)
hwdot1qVlanStatEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwdot1qVlanStatEnableStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LswSMON-MIB",
    **{"hwSmonExtend": hwSmonExtend,
       "smonExtendObject": smonExtendObject,
       "hwdot1qVlanStatNumber": hwdot1qVlanStatNumber,
       "hwdot1qVlanStatStatusTable": hwdot1qVlanStatStatusTable,
       "hwdot1qVlanStatStatusEntry": hwdot1qVlanStatStatusEntry,
       "hwdot1qVlanStatEnableIndex": hwdot1qVlanStatEnableIndex,
       "hwdot1qVlanStatEnableStatus": hwdot1qVlanStatEnableStatus}
)

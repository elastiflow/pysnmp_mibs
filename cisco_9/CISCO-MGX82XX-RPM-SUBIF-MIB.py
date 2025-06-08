# SNMP MIB module (CISCO-MGX82XX-RPM-SUBIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-MGX82XX-RPM-SUBIF-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:12:02 2025
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

(rpmPort,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "rpmPort")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoMgx82xxRpmSubIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 60)
)
if mibBuilder.loadTexts:
    ciscoMgx82xxRpmSubIfMIB.setRevisions(
        ("2002-09-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RpmPortTable_Object = MibTable
rpmPortTable = _RpmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rpmPortTable.setStatus("current")
_RpmPortEntry_Object = MibTableRow
rpmPortEntry = _RpmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1)
)
rpmPortEntry.setIndexNames(
    (0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"),
    (0, "CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"),
)
if mibBuilder.loadTexts:
    rpmPortEntry.setStatus("current")


class _RpmPortSlotNum_Type(Integer32):
    """Custom type rpmPortSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RpmPortSlotNum_Type.__name__ = "Integer32"
_RpmPortSlotNum_Object = MibTableColumn
rpmPortSlotNum = _RpmPortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 1),
    _RpmPortSlotNum_Type()
)
rpmPortSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmPortSlotNum.setStatus("current")


class _RpmPortInterface_Type(Integer32):
    """Custom type rpmPortInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RpmPortInterface_Type.__name__ = "Integer32"
_RpmPortInterface_Object = MibTableColumn
rpmPortInterface = _RpmPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 2),
    _RpmPortInterface_Type()
)
rpmPortInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmPortInterface.setStatus("current")


class _RpmPortSubInterface_Type(Integer32):
    """Custom type rpmPortSubInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RpmPortSubInterface_Type.__name__ = "Integer32"
_RpmPortSubInterface_Object = MibTableColumn
rpmPortSubInterface = _RpmPortSubInterface_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 3),
    _RpmPortSubInterface_Type()
)
rpmPortSubInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmPortSubInterface.setStatus("current")


class _RpmPortRowStatus_Type(Integer32):
    """Custom type rpmPortRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("del", 2),
          ("mod", 3))
    )


_RpmPortRowStatus_Type.__name__ = "Integer32"
_RpmPortRowStatus_Object = MibTableColumn
rpmPortRowStatus = _RpmPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 4),
    _RpmPortRowStatus_Type()
)
rpmPortRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmPortRowStatus.setStatus("current")
_RpmPortIpAddress_Type = IpAddress
_RpmPortIpAddress_Object = MibTableColumn
rpmPortIpAddress = _RpmPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 5),
    _RpmPortIpAddress_Type()
)
rpmPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmPortIpAddress.setStatus("current")
_RpmPortSubNetMask_Type = IpAddress
_RpmPortSubNetMask_Object = MibTableColumn
rpmPortSubNetMask = _RpmPortSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 6),
    _RpmPortSubNetMask_Type()
)
rpmPortSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmPortSubNetMask.setStatus("current")


class _RpmPortState_Type(Integer32):
    """Custom type rpmPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 1),
          ("active", 2),
          ("failed", 3))
    )


_RpmPortState_Type.__name__ = "Integer32"
_RpmPortState_Object = MibTableColumn
rpmPortState = _RpmPortState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 2, 9, 1, 1, 1, 7),
    _RpmPortState_Type()
)
rpmPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rpmPortState.setStatus("current")
_CmrSubIfMIBConformance_ObjectIdentity = ObjectIdentity
cmrSubIfMIBConformance = _CmrSubIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 60, 2)
)
_CmrSubIfMIBCompliances_ObjectIdentity = ObjectIdentity
cmrSubIfMIBCompliances = _CmrSubIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1)
)
_CmrSubIfMIBGroups_ObjectIdentity = ObjectIdentity
cmrSubIfMIBGroups = _CmrSubIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2)
)

# Managed Objects groups

cmrSubIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 2, 1)
)
cmrSubIfMIBGroup.setObjects(
      *(("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSlotNum"),
        ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortInterface"),
        ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubInterface"),
        ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortRowStatus"),
        ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortIpAddress"),
        ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortSubNetMask"),
        ("CISCO-MGX82XX-RPM-SUBIF-MIB", "rpmPortState"))
)
if mibBuilder.loadTexts:
    cmrSubIfMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmrSubIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 60, 2, 1, 1)
)
cmrSubIfMIBCompliance.setObjects(
    ("CISCO-MGX82XX-RPM-SUBIF-MIB", "cmrSubIfMIBGroup")
)
if mibBuilder.loadTexts:
    cmrSubIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-RPM-SUBIF-MIB",
    **{"rpmPortTable": rpmPortTable,
       "rpmPortEntry": rpmPortEntry,
       "rpmPortSlotNum": rpmPortSlotNum,
       "rpmPortInterface": rpmPortInterface,
       "rpmPortSubInterface": rpmPortSubInterface,
       "rpmPortRowStatus": rpmPortRowStatus,
       "rpmPortIpAddress": rpmPortIpAddress,
       "rpmPortSubNetMask": rpmPortSubNetMask,
       "rpmPortState": rpmPortState,
       "ciscoMgx82xxRpmSubIfMIB": ciscoMgx82xxRpmSubIfMIB,
       "cmrSubIfMIBConformance": cmrSubIfMIBConformance,
       "cmrSubIfMIBCompliances": cmrSubIfMIBCompliances,
       "cmrSubIfMIBCompliance": cmrSubIfMIBCompliance,
       "cmrSubIfMIBGroups": cmrSubIfMIBGroups,
       "cmrSubIfMIBGroup": cmrSubIfMIBGroup}
)

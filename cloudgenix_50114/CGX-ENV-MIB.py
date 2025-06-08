# SNMP MIB module (CGX-ENV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cloudgenix_50114/CGX-ENV-MIB.mib
# Produced by pysmi-1.6.1 at Wed Jun  4 13:56:22 2025
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

(CgxDegreesC,
 CgxVolts,
 cgxMgmt) = mibBuilder.importSymbols(
    "CLOUDGENIX-SMI",
    "CgxDegreesC",
    "CgxVolts",
    "cgxMgmt")

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

cgxEnvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CgxEnvAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("nonConfigurable", 3))
    )



class CgxEnvStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("notPresent", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CgxEnvNotifications_ObjectIdentity = ObjectIdentity
cgxEnvNotifications = _CgxEnvNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 0)
)
_CgxEnvObjects_ObjectIdentity = ObjectIdentity
cgxEnvObjects = _CgxEnvObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 1)
)
_CgxEnvStats_ObjectIdentity = ObjectIdentity
cgxEnvStats = _CgxEnvStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 1, 1)
)
_CgxEnvConfig_ObjectIdentity = ObjectIdentity
cgxEnvConfig = _CgxEnvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 1, 2)
)
_CgxEnvConformance_ObjectIdentity = ObjectIdentity
cgxEnvConformance = _CgxEnvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2)
)
_CgxEnvCompliances_ObjectIdentity = ObjectIdentity
cgxEnvCompliances = _CgxEnvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 1)
)
_CgxEnvGroups_ObjectIdentity = ObjectIdentity
cgxEnvGroups = _CgxEnvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 2)
)
_CgxEnvData_ObjectIdentity = ObjectIdentity
cgxEnvData = _CgxEnvData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10)
)
if mibBuilder.loadTexts:
    cgxEnvData.setStatus("current")
_CgxEnvNumFans_Type = Unsigned32
_CgxEnvNumFans_Object = MibScalar
cgxEnvNumFans = _CgxEnvNumFans_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 10),
    _CgxEnvNumFans_Type()
)
cgxEnvNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvNumFans.setStatus("current")
_CgxEnvFanTable_Object = MibTable
cgxEnvFanTable = _CgxEnvFanTable_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 11)
)
if mibBuilder.loadTexts:
    cgxEnvFanTable.setStatus("current")
_CgxEnvFanEntry_Object = MibTableRow
cgxEnvFanEntry = _CgxEnvFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 11, 1)
)
cgxEnvFanEntry.setIndexNames(
    (0, "CGX-ENV-MIB", "cgxEnvFanIndex"),
)
if mibBuilder.loadTexts:
    cgxEnvFanEntry.setStatus("current")
_CgxEnvFanIndex_Type = Unsigned32
_CgxEnvFanIndex_Object = MibTableColumn
cgxEnvFanIndex = _CgxEnvFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 11, 1, 1),
    _CgxEnvFanIndex_Type()
)
cgxEnvFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvFanIndex.setStatus("current")
_CgxEnvFanName_Type = DisplayString
_CgxEnvFanName_Object = MibTableColumn
cgxEnvFanName = _CgxEnvFanName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 11, 1, 2),
    _CgxEnvFanName_Type()
)
cgxEnvFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvFanName.setStatus("current")
_CgxEnvFanStatus_Type = CgxEnvStatus
_CgxEnvFanStatus_Object = MibTableColumn
cgxEnvFanStatus = _CgxEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 11, 1, 3),
    _CgxEnvFanStatus_Type()
)
cgxEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvFanStatus.setStatus("current")
_CgxEnvFanSpeed_Type = Integer32
_CgxEnvFanSpeed_Object = MibTableColumn
cgxEnvFanSpeed = _CgxEnvFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 11, 1, 4),
    _CgxEnvFanSpeed_Type()
)
cgxEnvFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cgxEnvFanSpeed.setUnits("RPM")
_CgxEnvFanAdminState_Type = CgxEnvAdminState
_CgxEnvFanAdminState_Object = MibTableColumn
cgxEnvFanAdminState = _CgxEnvFanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 11, 1, 5),
    _CgxEnvFanAdminState_Type()
)
cgxEnvFanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvFanAdminState.setStatus("current")
_CgxEnvNumPsu_Type = Unsigned32
_CgxEnvNumPsu_Object = MibScalar
cgxEnvNumPsu = _CgxEnvNumPsu_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 20),
    _CgxEnvNumPsu_Type()
)
cgxEnvNumPsu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvNumPsu.setStatus("current")
_CgxEnvPsuTable_Object = MibTable
cgxEnvPsuTable = _CgxEnvPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 21)
)
if mibBuilder.loadTexts:
    cgxEnvPsuTable.setStatus("current")
_CgxEnvPsuEntry_Object = MibTableRow
cgxEnvPsuEntry = _CgxEnvPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 21, 1)
)
cgxEnvPsuEntry.setIndexNames(
    (0, "CGX-ENV-MIB", "cgxEnvPsuTableIndex"),
)
if mibBuilder.loadTexts:
    cgxEnvPsuEntry.setStatus("current")
_CgxEnvPsuTableIndex_Type = Unsigned32
_CgxEnvPsuTableIndex_Object = MibTableColumn
cgxEnvPsuTableIndex = _CgxEnvPsuTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 21, 1, 1),
    _CgxEnvPsuTableIndex_Type()
)
cgxEnvPsuTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPsuTableIndex.setStatus("current")
_CgxEnvPsuTableName_Type = DisplayString
_CgxEnvPsuTableName_Object = MibTableColumn
cgxEnvPsuTableName = _CgxEnvPsuTableName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 21, 1, 2),
    _CgxEnvPsuTableName_Type()
)
cgxEnvPsuTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPsuTableName.setStatus("current")
_CgxEnvPsuTableStatus_Type = CgxEnvStatus
_CgxEnvPsuTableStatus_Object = MibTableColumn
cgxEnvPsuTableStatus = _CgxEnvPsuTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 21, 1, 3),
    _CgxEnvPsuTableStatus_Type()
)
cgxEnvPsuTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPsuTableStatus.setStatus("current")
_CgxEnvPsuTableAdminState_Type = CgxEnvAdminState
_CgxEnvPsuTableAdminState_Object = MibTableColumn
cgxEnvPsuTableAdminState = _CgxEnvPsuTableAdminState_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 21, 1, 4),
    _CgxEnvPsuTableAdminState_Type()
)
cgxEnvPsuTableAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPsuTableAdminState.setStatus("current")
_CgxEnvNumTemp_Type = Unsigned32
_CgxEnvNumTemp_Object = MibScalar
cgxEnvNumTemp = _CgxEnvNumTemp_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 30),
    _CgxEnvNumTemp_Type()
)
cgxEnvNumTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvNumTemp.setStatus("current")
_CgxEnvTempTable_Object = MibTable
cgxEnvTempTable = _CgxEnvTempTable_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 31)
)
if mibBuilder.loadTexts:
    cgxEnvTempTable.setStatus("current")
_CgxEnvTempEntry_Object = MibTableRow
cgxEnvTempEntry = _CgxEnvTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 31, 1)
)
cgxEnvTempEntry.setIndexNames(
    (0, "CGX-ENV-MIB", "cgxEnvTempIndex"),
)
if mibBuilder.loadTexts:
    cgxEnvTempEntry.setStatus("current")
_CgxEnvTempIndex_Type = Unsigned32
_CgxEnvTempIndex_Object = MibTableColumn
cgxEnvTempIndex = _CgxEnvTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 31, 1, 1),
    _CgxEnvTempIndex_Type()
)
cgxEnvTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvTempIndex.setStatus("current")
_CgxEnvTempName_Type = DisplayString
_CgxEnvTempName_Object = MibTableColumn
cgxEnvTempName = _CgxEnvTempName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 31, 1, 2),
    _CgxEnvTempName_Type()
)
cgxEnvTempName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvTempName.setStatus("current")
_CgxEnvTempStatus_Type = CgxEnvStatus
_CgxEnvTempStatus_Object = MibTableColumn
cgxEnvTempStatus = _CgxEnvTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 31, 1, 3),
    _CgxEnvTempStatus_Type()
)
cgxEnvTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvTempStatus.setStatus("current")
_CgxEnvTempReading_Type = CgxDegreesC
_CgxEnvTempReading_Object = MibTableColumn
cgxEnvTempReading = _CgxEnvTempReading_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 31, 1, 4),
    _CgxEnvTempReading_Type()
)
cgxEnvTempReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvTempReading.setStatus("current")
if mibBuilder.loadTexts:
    cgxEnvTempReading.setUnits("C")
_CgxEnvTempAdminState_Type = CgxEnvAdminState
_CgxEnvTempAdminState_Object = MibTableColumn
cgxEnvTempAdminState = _CgxEnvTempAdminState_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 31, 1, 5),
    _CgxEnvTempAdminState_Type()
)
cgxEnvTempAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvTempAdminState.setStatus("current")
_CgxEnvNumPower_Type = Unsigned32
_CgxEnvNumPower_Object = MibScalar
cgxEnvNumPower = _CgxEnvNumPower_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 40),
    _CgxEnvNumPower_Type()
)
cgxEnvNumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvNumPower.setStatus("current")
_CgxEnvPowerTable_Object = MibTable
cgxEnvPowerTable = _CgxEnvPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 41)
)
if mibBuilder.loadTexts:
    cgxEnvPowerTable.setStatus("current")
_CgxEnvPowerEntry_Object = MibTableRow
cgxEnvPowerEntry = _CgxEnvPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 41, 1)
)
cgxEnvPowerEntry.setIndexNames(
    (0, "CGX-ENV-MIB", "cgxEnvPowerIndex"),
)
if mibBuilder.loadTexts:
    cgxEnvPowerEntry.setStatus("current")
_CgxEnvPowerIndex_Type = Unsigned32
_CgxEnvPowerIndex_Object = MibTableColumn
cgxEnvPowerIndex = _CgxEnvPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 41, 1, 1),
    _CgxEnvPowerIndex_Type()
)
cgxEnvPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPowerIndex.setStatus("current")
_CgxEnvPowerName_Type = DisplayString
_CgxEnvPowerName_Object = MibTableColumn
cgxEnvPowerName = _CgxEnvPowerName_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 41, 1, 2),
    _CgxEnvPowerName_Type()
)
cgxEnvPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPowerName.setStatus("current")
_CgxEnvPowerStatus_Type = CgxEnvStatus
_CgxEnvPowerStatus_Object = MibTableColumn
cgxEnvPowerStatus = _CgxEnvPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 41, 1, 3),
    _CgxEnvPowerStatus_Type()
)
cgxEnvPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPowerStatus.setStatus("current")
_CgxEnvPowerVoltage_Type = CgxVolts
_CgxEnvPowerVoltage_Object = MibTableColumn
cgxEnvPowerVoltage = _CgxEnvPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 41, 1, 4),
    _CgxEnvPowerVoltage_Type()
)
cgxEnvPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPowerVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cgxEnvPowerVoltage.setUnits("V")
_CgxEnvPowerAdminState_Type = CgxEnvAdminState
_CgxEnvPowerAdminState_Object = MibTableColumn
cgxEnvPowerAdminState = _CgxEnvPowerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 10, 41, 1, 5),
    _CgxEnvPowerAdminState_Type()
)
cgxEnvPowerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgxEnvPowerAdminState.setStatus("current")

# Managed Objects groups

cgxEnvObjectNumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 2, 1)
)
cgxEnvObjectNumGroup.setObjects(
      *(("CGX-ENV-MIB", "cgxEnvNumFans"),
        ("CGX-ENV-MIB", "cgxEnvNumPower"),
        ("CGX-ENV-MIB", "cgxEnvNumPsu"),
        ("CGX-ENV-MIB", "cgxEnvNumTemp"))
)
if mibBuilder.loadTexts:
    cgxEnvObjectNumGroup.setStatus("current")

cgxEnvFanEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 2, 2)
)
cgxEnvFanEntryGroup.setObjects(
      *(("CGX-ENV-MIB", "cgxEnvFanAdminState"),
        ("CGX-ENV-MIB", "cgxEnvFanIndex"),
        ("CGX-ENV-MIB", "cgxEnvFanName"),
        ("CGX-ENV-MIB", "cgxEnvFanSpeed"),
        ("CGX-ENV-MIB", "cgxEnvFanStatus"))
)
if mibBuilder.loadTexts:
    cgxEnvFanEntryGroup.setStatus("current")

cgxEnvPsuEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 2, 3)
)
cgxEnvPsuEntryGroup.setObjects(
      *(("CGX-ENV-MIB", "cgxEnvPsuTableAdminState"),
        ("CGX-ENV-MIB", "cgxEnvPsuTableIndex"),
        ("CGX-ENV-MIB", "cgxEnvPsuTableName"),
        ("CGX-ENV-MIB", "cgxEnvPsuTableStatus"))
)
if mibBuilder.loadTexts:
    cgxEnvPsuEntryGroup.setStatus("current")

cgxEnvTempEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 2, 4)
)
cgxEnvTempEntryGroup.setObjects(
      *(("CGX-ENV-MIB", "cgxEnvTempAdminState"),
        ("CGX-ENV-MIB", "cgxEnvTempIndex"),
        ("CGX-ENV-MIB", "cgxEnvTempName"),
        ("CGX-ENV-MIB", "cgxEnvTempReading"),
        ("CGX-ENV-MIB", "cgxEnvTempStatus"))
)
if mibBuilder.loadTexts:
    cgxEnvTempEntryGroup.setStatus("current")

cgxEnvPowerEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 2, 5)
)
cgxEnvPowerEntryGroup.setObjects(
      *(("CGX-ENV-MIB", "cgxEnvPowerAdminState"),
        ("CGX-ENV-MIB", "cgxEnvPowerIndex"),
        ("CGX-ENV-MIB", "cgxEnvPowerName"),
        ("CGX-ENV-MIB", "cgxEnvPowerStatus"),
        ("CGX-ENV-MIB", "cgxEnvPowerVoltage"))
)
if mibBuilder.loadTexts:
    cgxEnvPowerEntryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cgxEnvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 50114, 10, 3, 2, 1, 1)
)
cgxEnvMIBCompliance.setObjects(
      *(("CGX-ENV-MIB", "cgxEnvFanEntryGroup"),
        ("CGX-ENV-MIB", "cgxEnvObjectNumGroup"),
        ("CGX-ENV-MIB", "cgxEnvPowerEntryGroup"),
        ("CGX-ENV-MIB", "cgxEnvPsuEntryGroup"),
        ("CGX-ENV-MIB", "cgxEnvTempEntryGroup"))
)
if mibBuilder.loadTexts:
    cgxEnvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CGX-ENV-MIB",
    **{"CgxEnvAdminState": CgxEnvAdminState,
       "CgxEnvStatus": CgxEnvStatus,
       "cgxEnvMIB": cgxEnvMIB,
       "cgxEnvNotifications": cgxEnvNotifications,
       "cgxEnvObjects": cgxEnvObjects,
       "cgxEnvStats": cgxEnvStats,
       "cgxEnvConfig": cgxEnvConfig,
       "cgxEnvConformance": cgxEnvConformance,
       "cgxEnvCompliances": cgxEnvCompliances,
       "cgxEnvMIBCompliance": cgxEnvMIBCompliance,
       "cgxEnvGroups": cgxEnvGroups,
       "cgxEnvObjectNumGroup": cgxEnvObjectNumGroup,
       "cgxEnvFanEntryGroup": cgxEnvFanEntryGroup,
       "cgxEnvPsuEntryGroup": cgxEnvPsuEntryGroup,
       "cgxEnvTempEntryGroup": cgxEnvTempEntryGroup,
       "cgxEnvPowerEntryGroup": cgxEnvPowerEntryGroup,
       "cgxEnvData": cgxEnvData,
       "cgxEnvNumFans": cgxEnvNumFans,
       "cgxEnvFanTable": cgxEnvFanTable,
       "cgxEnvFanEntry": cgxEnvFanEntry,
       "cgxEnvFanIndex": cgxEnvFanIndex,
       "cgxEnvFanName": cgxEnvFanName,
       "cgxEnvFanStatus": cgxEnvFanStatus,
       "cgxEnvFanSpeed": cgxEnvFanSpeed,
       "cgxEnvFanAdminState": cgxEnvFanAdminState,
       "cgxEnvNumPsu": cgxEnvNumPsu,
       "cgxEnvPsuTable": cgxEnvPsuTable,
       "cgxEnvPsuEntry": cgxEnvPsuEntry,
       "cgxEnvPsuTableIndex": cgxEnvPsuTableIndex,
       "cgxEnvPsuTableName": cgxEnvPsuTableName,
       "cgxEnvPsuTableStatus": cgxEnvPsuTableStatus,
       "cgxEnvPsuTableAdminState": cgxEnvPsuTableAdminState,
       "cgxEnvNumTemp": cgxEnvNumTemp,
       "cgxEnvTempTable": cgxEnvTempTable,
       "cgxEnvTempEntry": cgxEnvTempEntry,
       "cgxEnvTempIndex": cgxEnvTempIndex,
       "cgxEnvTempName": cgxEnvTempName,
       "cgxEnvTempStatus": cgxEnvTempStatus,
       "cgxEnvTempReading": cgxEnvTempReading,
       "cgxEnvTempAdminState": cgxEnvTempAdminState,
       "cgxEnvNumPower": cgxEnvNumPower,
       "cgxEnvPowerTable": cgxEnvPowerTable,
       "cgxEnvPowerEntry": cgxEnvPowerEntry,
       "cgxEnvPowerIndex": cgxEnvPowerIndex,
       "cgxEnvPowerName": cgxEnvPowerName,
       "cgxEnvPowerStatus": cgxEnvPowerStatus,
       "cgxEnvPowerVoltage": cgxEnvPowerVoltage,
       "cgxEnvPowerAdminState": cgxEnvPowerAdminState}
)

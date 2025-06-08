# SNMP MIB module (RUIJIE-TM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-TM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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

ruijieTMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91)
)
if mibBuilder.loadTexts:
    ruijieTMMIB.setRevisions(
        ("2010-12-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieTMMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTMMIBObjects = _RuijieTMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1)
)
_RuijieTMQosDramMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTMQosDramMIBObjects = _RuijieTMQosDramMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 1)
)
_RuijieQosDramTable_Object = MibTable
ruijieQosDramTable = _RuijieQosDramTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieQosDramTable.setStatus("current")
_RuijieQosDramEntry_Object = MibTableRow
ruijieQosDramEntry = _RuijieQosDramEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 1, 1, 1)
)
ruijieQosDramEntry.setIndexNames(
    (0, "RUIJIE-TM-MIB", "ruijieQoSDramIndex"),
)
if mibBuilder.loadTexts:
    ruijieQosDramEntry.setStatus("current")
_RuijieQoSDramIndex_Type = Integer32
_RuijieQoSDramIndex_Object = MibTableColumn
ruijieQoSDramIndex = _RuijieQoSDramIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 1, 1, 1, 1),
    _RuijieQoSDramIndex_Type()
)
ruijieQoSDramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDramIndex.setStatus("current")
_RuijieQosDramTotal_Type = Integer32
_RuijieQosDramTotal_Object = MibTableColumn
ruijieQosDramTotal = _RuijieQosDramTotal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 1, 1, 1, 2),
    _RuijieQosDramTotal_Type()
)
ruijieQosDramTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosDramTotal.setStatus("current")
_RuijieQosDramCurUsed_Type = Integer32
_RuijieQosDramCurUsed_Object = MibTableColumn
ruijieQosDramCurUsed = _RuijieQosDramCurUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 1, 1, 1, 3),
    _RuijieQosDramCurUsed_Type()
)
ruijieQosDramCurUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQosDramCurUsed.setStatus("current")
_RuijieTMQosDropMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTMQosDropMIBObjects = _RuijieTMQosDropMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2)
)
_RuijieQosDropTable_Object = MibTable
ruijieQosDropTable = _RuijieQosDropTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruijieQosDropTable.setStatus("current")
_RuijieQosDropEntry_Object = MibTableRow
ruijieQosDropEntry = _RuijieQosDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1)
)
ruijieQosDropEntry.setIndexNames(
    (0, "RUIJIE-TM-MIB", "ruijieQoSDropIndex"),
)
if mibBuilder.loadTexts:
    ruijieQosDropEntry.setStatus("current")
_RuijieQoSDropIndex_Type = Integer32
_RuijieQoSDropIndex_Object = MibTableColumn
ruijieQoSDropIndex = _RuijieQoSDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 1),
    _RuijieQoSDropIndex_Type()
)
ruijieQoSDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDropIndex.setStatus("current")
_RuijieQoSTotalEnQue_Type = Integer32
_RuijieQoSTotalEnQue_Object = MibTableColumn
ruijieQoSTotalEnQue = _RuijieQoSTotalEnQue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 2),
    _RuijieQoSTotalEnQue_Type()
)
ruijieQoSTotalEnQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSTotalEnQue.setStatus("current")
_RuijieQoSTotalDeQue_Type = Integer32
_RuijieQoSTotalDeQue_Object = MibTableColumn
ruijieQoSTotalDeQue = _RuijieQoSTotalDeQue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 3),
    _RuijieQoSTotalDeQue_Type()
)
ruijieQoSTotalDeQue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSTotalDeQue.setStatus("current")
_RuijieQoSEnQueDrop_Type = Integer32
_RuijieQoSEnQueDrop_Object = MibTableColumn
ruijieQoSEnQueDrop = _RuijieQoSEnQueDrop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 4),
    _RuijieQoSEnQueDrop_Type()
)
ruijieQoSEnQueDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSEnQueDrop.setStatus("current")
_RuijieQoSEnQueDropByBuf_Type = Integer32
_RuijieQoSEnQueDropByBuf_Object = MibTableColumn
ruijieQoSEnQueDropByBuf = _RuijieQoSEnQueDropByBuf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 5),
    _RuijieQoSEnQueDropByBuf_Type()
)
ruijieQoSEnQueDropByBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSEnQueDropByBuf.setStatus("current")
_RuijieQoSEnQueDropByBufDesc_Type = Integer32
_RuijieQoSEnQueDropByBufDesc_Object = MibTableColumn
ruijieQoSEnQueDropByBufDesc = _RuijieQoSEnQueDropByBufDesc_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 6),
    _RuijieQoSEnQueDropByBufDesc_Type()
)
ruijieQoSEnQueDropByBufDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSEnQueDropByBufDesc.setStatus("current")
_RuijieQoSEnQueDropByOther_Type = Integer32
_RuijieQoSEnQueDropByOther_Object = MibTableColumn
ruijieQoSEnQueDropByOther = _RuijieQoSEnQueDropByOther_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 7),
    _RuijieQoSEnQueDropByOther_Type()
)
ruijieQoSEnQueDropByOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSEnQueDropByOther.setStatus("current")
_RuijieQoSDeQueDrop_Type = Integer32
_RuijieQoSDeQueDrop_Object = MibTableColumn
ruijieQoSDeQueDrop = _RuijieQoSDeQueDrop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 8),
    _RuijieQoSDeQueDrop_Type()
)
ruijieQoSDeQueDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSDeQueDrop.setStatus("current")
_RuijieQoSLastClearTime_Type = TimeTicks
_RuijieQoSLastClearTime_Object = MibTableColumn
ruijieQoSLastClearTime = _RuijieQoSLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 2, 1, 1, 9),
    _RuijieQoSLastClearTime_Type()
)
ruijieQoSLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSLastClearTime.setStatus("current")
_RuijieTMQosQueMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTMQosQueMIBObjects = _RuijieTMQosQueMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3)
)
_RuijieQosQueTable_Object = MibTable
ruijieQosQueTable = _RuijieQosQueTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruijieQosQueTable.setStatus("current")
_RuijieQosQueEntry_Object = MibTableRow
ruijieQosQueEntry = _RuijieQosQueEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1)
)
ruijieQosQueEntry.setIndexNames(
    (0, "RUIJIE-TM-MIB", "ruijieQoSIfIndex"),
    (0, "RUIJIE-TM-MIB", "ruijieQoSIfChipIndex"),
    (0, "RUIJIE-TM-MIB", "ruijieQoSIfChipQueIndex"),
)
if mibBuilder.loadTexts:
    ruijieQosQueEntry.setStatus("current")
_RuijieQoSIfIndex_Type = IfIndex
_RuijieQoSIfIndex_Object = MibTableColumn
ruijieQoSIfIndex = _RuijieQoSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 1),
    _RuijieQoSIfIndex_Type()
)
ruijieQoSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfIndex.setStatus("current")


class _RuijieQoSIfChipIndex_Type(Integer32):
    """Custom type ruijieQoSIfChipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("chip-0", 0),
          ("chip-1", 1))
    )


_RuijieQoSIfChipIndex_Type.__name__ = "Integer32"
_RuijieQoSIfChipIndex_Object = MibTableColumn
ruijieQoSIfChipIndex = _RuijieQoSIfChipIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 2),
    _RuijieQoSIfChipIndex_Type()
)
ruijieQoSIfChipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfChipIndex.setStatus("current")


class _RuijieQoSIfChipQueIndex_Type(Integer32):
    """Custom type ruijieQoSIfChipQueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("queue-1", 1),
          ("queue-2", 2),
          ("queue-3", 3),
          ("queue-4", 4),
          ("queue-5", 5),
          ("queue-6", 6),
          ("queue-7", 7),
          ("queue-8", 8))
    )


_RuijieQoSIfChipQueIndex_Type.__name__ = "Integer32"
_RuijieQoSIfChipQueIndex_Object = MibTableColumn
ruijieQoSIfChipQueIndex = _RuijieQoSIfChipQueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 3),
    _RuijieQoSIfChipQueIndex_Type()
)
ruijieQoSIfChipQueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfChipQueIndex.setStatus("current")
_RuijieQoSIfChipMax_Type = Integer32
_RuijieQoSIfChipMax_Object = MibTableColumn
ruijieQoSIfChipMax = _RuijieQoSIfChipMax_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 4),
    _RuijieQoSIfChipMax_Type()
)
ruijieQoSIfChipMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfChipMax.setStatus("current")
_RuijieQoSIfChipCur_Type = Integer32
_RuijieQoSIfChipCur_Object = MibTableColumn
ruijieQoSIfChipCur = _RuijieQoSIfChipCur_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 5),
    _RuijieQoSIfChipCur_Type()
)
ruijieQoSIfChipCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfChipCur.setStatus("current")
_RuijieQoSIfChipPeak_Type = Integer32
_RuijieQoSIfChipPeak_Object = MibTableColumn
ruijieQoSIfChipPeak = _RuijieQoSIfChipPeak_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 6),
    _RuijieQoSIfChipPeak_Type()
)
ruijieQoSIfChipPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfChipPeak.setStatus("current")
_RuijieQoSIfChipRate_Type = Integer32
_RuijieQoSIfChipRate_Object = MibTableColumn
ruijieQoSIfChipRate = _RuijieQoSIfChipRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 7),
    _RuijieQoSIfChipRate_Type()
)
ruijieQoSIfChipRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfChipRate.setStatus("current")
_RuijieQoSIfChipTime_Type = TimeTicks
_RuijieQoSIfChipTime_Object = MibTableColumn
ruijieQoSIfChipTime = _RuijieQoSIfChipTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 1, 3, 1, 1, 8),
    _RuijieQoSIfChipTime_Type()
)
ruijieQoSIfChipTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieQoSIfChipTime.setStatus("current")
_RuijieTMMIBConformance_ObjectIdentity = ObjectIdentity
ruijieTMMIBConformance = _RuijieTMMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 2)
)
_RuijieTMMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieTMMIBCompliances = _RuijieTMMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 2, 1)
)
_RuijieTMMIBGroups_ObjectIdentity = ObjectIdentity
ruijieTMMIBGroups = _RuijieTMMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 2, 2)
)

# Managed Objects groups

ruijieTMMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 2, 2, 1)
)
ruijieTMMIBGroup.setObjects(
      *(("RUIJIE-TM-MIB", "ruijieQoSDramIndex"),
        ("RUIJIE-TM-MIB", "ruijieQosDramTotal"),
        ("RUIJIE-TM-MIB", "ruijieQosDramCurUsed"),
        ("RUIJIE-TM-MIB", "ruijieQoSDropIndex"),
        ("RUIJIE-TM-MIB", "ruijieQoSTotalEnQue"),
        ("RUIJIE-TM-MIB", "ruijieQoSTotalDeQue"),
        ("RUIJIE-TM-MIB", "ruijieQoSEnQueDrop"),
        ("RUIJIE-TM-MIB", "ruijieQoSEnQueDropByBuf"),
        ("RUIJIE-TM-MIB", "ruijieQoSEnQueDropByBufDesc"),
        ("RUIJIE-TM-MIB", "ruijieQoSEnQueDropByOther"),
        ("RUIJIE-TM-MIB", "ruijieQoSDeQueDrop"),
        ("RUIJIE-TM-MIB", "ruijieQoSLastClearTime"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfIndex"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfChipIndex"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfChipQueIndex"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfChipMax"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfChipCur"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfChipPeak"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfChipRate"),
        ("RUIJIE-TM-MIB", "ruijieQoSIfChipTime"))
)
if mibBuilder.loadTexts:
    ruijieTMMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieTMMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 91, 2, 1, 1)
)
ruijieTMMIBCompliance.setObjects(
    ("RUIJIE-TM-MIB", "ruijieTMMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieTMMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-TM-MIB",
    **{"ruijieTMMIB": ruijieTMMIB,
       "ruijieTMMIBObjects": ruijieTMMIBObjects,
       "ruijieTMQosDramMIBObjects": ruijieTMQosDramMIBObjects,
       "ruijieQosDramTable": ruijieQosDramTable,
       "ruijieQosDramEntry": ruijieQosDramEntry,
       "ruijieQoSDramIndex": ruijieQoSDramIndex,
       "ruijieQosDramTotal": ruijieQosDramTotal,
       "ruijieQosDramCurUsed": ruijieQosDramCurUsed,
       "ruijieTMQosDropMIBObjects": ruijieTMQosDropMIBObjects,
       "ruijieQosDropTable": ruijieQosDropTable,
       "ruijieQosDropEntry": ruijieQosDropEntry,
       "ruijieQoSDropIndex": ruijieQoSDropIndex,
       "ruijieQoSTotalEnQue": ruijieQoSTotalEnQue,
       "ruijieQoSTotalDeQue": ruijieQoSTotalDeQue,
       "ruijieQoSEnQueDrop": ruijieQoSEnQueDrop,
       "ruijieQoSEnQueDropByBuf": ruijieQoSEnQueDropByBuf,
       "ruijieQoSEnQueDropByBufDesc": ruijieQoSEnQueDropByBufDesc,
       "ruijieQoSEnQueDropByOther": ruijieQoSEnQueDropByOther,
       "ruijieQoSDeQueDrop": ruijieQoSDeQueDrop,
       "ruijieQoSLastClearTime": ruijieQoSLastClearTime,
       "ruijieTMQosQueMIBObjects": ruijieTMQosQueMIBObjects,
       "ruijieQosQueTable": ruijieQosQueTable,
       "ruijieQosQueEntry": ruijieQosQueEntry,
       "ruijieQoSIfIndex": ruijieQoSIfIndex,
       "ruijieQoSIfChipIndex": ruijieQoSIfChipIndex,
       "ruijieQoSIfChipQueIndex": ruijieQoSIfChipQueIndex,
       "ruijieQoSIfChipMax": ruijieQoSIfChipMax,
       "ruijieQoSIfChipCur": ruijieQoSIfChipCur,
       "ruijieQoSIfChipPeak": ruijieQoSIfChipPeak,
       "ruijieQoSIfChipRate": ruijieQoSIfChipRate,
       "ruijieQoSIfChipTime": ruijieQoSIfChipTime,
       "ruijieTMMIBConformance": ruijieTMMIBConformance,
       "ruijieTMMIBCompliances": ruijieTMMIBCompliances,
       "ruijieTMMIBCompliance": ruijieTMMIBCompliance,
       "ruijieTMMIBGroups": ruijieTMMIBGroups,
       "ruijieTMMIBGroup": ruijieTMMIBGroup}
)

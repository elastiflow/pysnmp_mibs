# SNMP MIB module (ZHONE-SECHTOR300-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zhone_5504/ZHONE-SECHTOR300-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:11:11 2025
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

(dsx1ConfigEntry,
 dsx1LineIndex) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1ConfigEntry",
    "dsx1LineIndex")

(dsx3ConfigEntry,
 dsx3LineIndex) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3ConfigEntry",
    "dsx3LineIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(sechtor300,
 zhoneModules,
 zhoneShelfIndex,
 zhoneSlotIndex) = mibBuilder.importSymbols(
    "Zhone",
    "sechtor300",
    "zhoneModules",
    "zhoneShelfIndex",
    "zhoneSlotIndex")

(ZhoneAdminString,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhoneSechtor300 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 28)
)
if mibBuilder.loadTexts:
    zhoneSechtor300.setRevisions(
        ("2004-04-23 13:35",
         "2004-03-18 15:23",
         "2003-08-26 12:05",
         "2001-11-14 14:45",
         "2001-11-08 14:29",
         "2001-09-27 14:31",
         "2001-09-18 07:33",
         "2001-08-02 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ZhoneABCDValue(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("abcd0000", 1),
          ("abcd0001", 2),
          ("abcd0010", 3),
          ("abcd0011", 4),
          ("abcd0100", 5),
          ("abcd0101", 6),
          ("abcd0110", 7),
          ("abcd0111", 8),
          ("abcd1000", 9),
          ("abcd1001", 10),
          ("abcd1010", 11),
          ("abcd1011", 12),
          ("abcd1100", 13),
          ("abcd1101", 14),
          ("abcd1110", 15),
          ("abcd1111", 16))
    )



# MIB Managed Objects in the order of their OIDs

_S300Equipment_ObjectIdentity = ObjectIdentity
s300Equipment = _S300Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    s300Equipment.setStatus("current")
_S300IOCardResourceTable_Object = MibTable
s300IOCardResourceTable = _S300IOCardResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    s300IOCardResourceTable.setStatus("current")
_S300IOCardResourceEntry_Object = MibTableRow
s300IOCardResourceEntry = _S300IOCardResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1, 1)
)
s300IOCardResourceEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    s300IOCardResourceEntry.setStatus("current")
_S300IOCardIdentification_Type = ZhoneAdminString
_S300IOCardIdentification_Object = MibTableColumn
s300IOCardIdentification = _S300IOCardIdentification_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1, 1, 1),
    _S300IOCardIdentification_Type()
)
s300IOCardIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300IOCardIdentification.setStatus("current")


class _S300IOCardZhoneType_Type(Integer32):
    """Custom type s300IOCardZhoneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6100,
              6101,
              6102,
              6103,
              6104,
              6105,
              6106,
              6107,
              6108,
              6109,
              6110,
              6111,
              6112,
              6113)
        )
    )
    namedValues = NamedValues(
        *(("unknownType", 1),
          ("s300T1E1IO", 6100),
          ("s300T1E1IOProtection", 6101),
          ("s300FxsRinger", 6102),
          ("s300FxoRinger", 6103),
          ("s300Stm1IODx", 6104),
          ("s300Stm1IOSx", 6105),
          ("s300Sts1IODx", 6106),
          ("s300Sts1IOSx", 6107),
          ("s300Ds3IODx", 6108),
          ("s300Ds3IOSx", 6109),
          ("s300Msu", 6110),
          ("s300Clkio", 6111),
          ("s300DualSts1IODx", 6112),
          ("s300DualSts1IOSx", 6113))
    )


_S300IOCardZhoneType_Type.__name__ = "Integer32"
_S300IOCardZhoneType_Object = MibTableColumn
s300IOCardZhoneType = _S300IOCardZhoneType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1, 1, 2),
    _S300IOCardZhoneType_Type()
)
s300IOCardZhoneType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300IOCardZhoneType.setStatus("current")
_S300IOCardMfgSerialNumber_Type = ZhoneAdminString
_S300IOCardMfgSerialNumber_Object = MibTableColumn
s300IOCardMfgSerialNumber = _S300IOCardMfgSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1, 1, 3),
    _S300IOCardMfgSerialNumber_Type()
)
s300IOCardMfgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300IOCardMfgSerialNumber.setStatus("current")
_S300IOCardMfgDate_Type = ZhoneAdminString
_S300IOCardMfgDate_Object = MibTableColumn
s300IOCardMfgDate = _S300IOCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1, 1, 4),
    _S300IOCardMfgDate_Type()
)
s300IOCardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300IOCardMfgDate.setStatus("current")
_S300IOCardProductNumber_Type = ZhoneAdminString
_S300IOCardProductNumber_Object = MibTableColumn
s300IOCardProductNumber = _S300IOCardProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1, 1, 5),
    _S300IOCardProductNumber_Type()
)
s300IOCardProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300IOCardProductNumber.setStatus("current")
_S300IOCardRevisionCode_Type = ZhoneAdminString
_S300IOCardRevisionCode_Object = MibTableColumn
s300IOCardRevisionCode = _S300IOCardRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 1, 1, 6),
    _S300IOCardRevisionCode_Type()
)
s300IOCardRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300IOCardRevisionCode.setStatus("current")
_S300EquipmentConfigTable_Object = MibTable
s300EquipmentConfigTable = _S300EquipmentConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    s300EquipmentConfigTable.setStatus("current")
_S300EquipmentConfigEntry_Object = MibTableRow
s300EquipmentConfigEntry = _S300EquipmentConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1)
)
s300EquipmentConfigEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    s300EquipmentConfigEntry.setStatus("current")


class _S300EquipmentType_Type(Integer32):
    """Custom type s300EquipmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6001,
              6002,
              6003,
              6004,
              6005,
              6006,
              6007,
              6008,
              6009,
              6010,
              6011,
              6110,
              6111)
        )
    )
    namedValues = NamedValues(
        *(("unknownType", 1),
          ("s300Cpu", 6001),
          ("s300St1Dsx", 6002),
          ("s300Se1", 6003),
          ("s300Mt3c", 6004),
          ("s300Sts1", 6005),
          ("s300Fxs", 6006),
          ("s300Fxo", 6007),
          ("s300S155", 6008),
          ("s300Ixcon", 6009),
          ("s300Xcon", 6010),
          ("s300St1Csu", 6011),
          ("s300Msu", 6110),
          ("s300Ckio", 6111))
    )


_S300EquipmentType_Type.__name__ = "Integer32"
_S300EquipmentType_Object = MibTableColumn
s300EquipmentType = _S300EquipmentType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 1),
    _S300EquipmentType_Type()
)
s300EquipmentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300EquipmentType.setStatus("current")


class _S300EquipmentMode_Type(Integer32):
    """Custom type s300EquipmentMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("s155Oc3", 2),
          ("s155Stm1", 3))
    )


_S300EquipmentMode_Type.__name__ = "Integer32"
_S300EquipmentMode_Object = MibTableColumn
s300EquipmentMode = _S300EquipmentMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 2),
    _S300EquipmentMode_Type()
)
s300EquipmentMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300EquipmentMode.setStatus("current")


class _S300EquipmentRedundancyMode_Type(Integer32):
    """Custom type s300EquipmentRedundancyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("simplex", 1),
          ("duplex", 2),
          ("oneplusone", 3),
          ("onetoN", 4),
          ("oneplusoneW", 5))
    )


_S300EquipmentRedundancyMode_Type.__name__ = "Integer32"
_S300EquipmentRedundancyMode_Object = MibTableColumn
s300EquipmentRedundancyMode = _S300EquipmentRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 3),
    _S300EquipmentRedundancyMode_Type()
)
s300EquipmentRedundancyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300EquipmentRedundancyMode.setStatus("current")


class _S300EquipmentPriority_Type(Integer32):
    """Custom type s300EquipmentPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_S300EquipmentPriority_Type.__name__ = "Integer32"
_S300EquipmentPriority_Object = MibTableColumn
s300EquipmentPriority = _S300EquipmentPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 4),
    _S300EquipmentPriority_Type()
)
s300EquipmentPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300EquipmentPriority.setStatus("current")


class _S300EquipmentWorkingMode_Type(Integer32):
    """Custom type s300EquipmentWorkingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("working", 1),
          ("protection", 2))
    )


_S300EquipmentWorkingMode_Type.__name__ = "Integer32"
_S300EquipmentWorkingMode_Object = MibTableColumn
s300EquipmentWorkingMode = _S300EquipmentWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 5),
    _S300EquipmentWorkingMode_Type()
)
s300EquipmentWorkingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300EquipmentWorkingMode.setStatus("current")


class _S300EquipmentAdminStatus_Type(Integer32):
    """Custom type s300EquipmentAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("maintenance", 2),
          ("reset", 3))
    )


_S300EquipmentAdminStatus_Type.__name__ = "Integer32"
_S300EquipmentAdminStatus_Object = MibTableColumn
s300EquipmentAdminStatus = _S300EquipmentAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 6),
    _S300EquipmentAdminStatus_Type()
)
s300EquipmentAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300EquipmentAdminStatus.setStatus("current")


class _S300EquipmentOperStatus_Type(Integer32):
    """Custom type s300EquipmentOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("unequipped", 2),
          ("fault", 3),
          ("maintenance", 4),
          ("initializing", 5))
    )


_S300EquipmentOperStatus_Type.__name__ = "Integer32"
_S300EquipmentOperStatus_Object = MibTableColumn
s300EquipmentOperStatus = _S300EquipmentOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 7),
    _S300EquipmentOperStatus_Type()
)
s300EquipmentOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300EquipmentOperStatus.setStatus("current")


class _S300EquipmentIOOperStatus_Type(Integer32):
    """Custom type s300EquipmentIOOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unequipped", 1),
          ("notrequired", 2),
          ("mismatch", 3),
          ("inservice", 4),
          ("fault", 5))
    )


_S300EquipmentIOOperStatus_Type.__name__ = "Integer32"
_S300EquipmentIOOperStatus_Object = MibTableColumn
s300EquipmentIOOperStatus = _S300EquipmentIOOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 8),
    _S300EquipmentIOOperStatus_Type()
)
s300EquipmentIOOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300EquipmentIOOperStatus.setStatus("current")


class _S300EquipmentFaultMap_Type(Bits):
    """Custom type s300EquipmentFaultMap based on Bits"""
    namedValues = NamedValues(
        *(("cardMissing", 0),
          ("cardMismatch", 1),
          ("ioCardMissing", 2),
          ("cardFailed", 3),
          ("majorHardwareFault", 4),
          ("majorSoftwareFault", 5),
          ("minorHardwareFault", 6),
          ("minorSoftwareFault", 7),
          ("peerHeartbeatFailure", 8),
          ("localHeartbeatFailure", 9),
          ("supervisorNotInitialized", 10),
          ("standbySynchronizationFailure", 11))
    )

_S300EquipmentFaultMap_Type.__name__ = "Bits"
_S300EquipmentFaultMap_Object = MibTableColumn
s300EquipmentFaultMap = _S300EquipmentFaultMap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 9),
    _S300EquipmentFaultMap_Type()
)
s300EquipmentFaultMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300EquipmentFaultMap.setStatus("current")
_S300EquipmentRowStatus_Type = ZhoneRowStatus
_S300EquipmentRowStatus_Object = MibTableColumn
s300EquipmentRowStatus = _S300EquipmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 2, 1, 10),
    _S300EquipmentRowStatus_Type()
)
s300EquipmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300EquipmentRowStatus.setStatus("current")
_S300EquipmentProtectionTable_Object = MibTable
s300EquipmentProtectionTable = _S300EquipmentProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    s300EquipmentProtectionTable.setStatus("current")
_S300EquipmentProtectionEntry_Object = MibTableRow
s300EquipmentProtectionEntry = _S300EquipmentProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 3, 1)
)
s300EquipmentProtectionEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
)
if mibBuilder.loadTexts:
    s300EquipmentProtectionEntry.setStatus("current")


class _S300EquipmentProtectionSlot_Type(Integer32):
    """Custom type s300EquipmentProtectionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_S300EquipmentProtectionSlot_Type.__name__ = "Integer32"
_S300EquipmentProtectionSlot_Object = MibTableColumn
s300EquipmentProtectionSlot = _S300EquipmentProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 3, 1, 1),
    _S300EquipmentProtectionSlot_Type()
)
s300EquipmentProtectionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300EquipmentProtectionSlot.setStatus("current")


class _S300EquipmentActiveSlot_Type(Integer32):
    """Custom type s300EquipmentActiveSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("working", 2),
          ("protection", 3))
    )


_S300EquipmentActiveSlot_Type.__name__ = "Integer32"
_S300EquipmentActiveSlot_Object = MibTableColumn
s300EquipmentActiveSlot = _S300EquipmentActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 3, 1, 2),
    _S300EquipmentActiveSlot_Type()
)
s300EquipmentActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300EquipmentActiveSlot.setStatus("current")


class _S300EquipmentSwitchAction_Type(Integer32):
    """Custom type s300EquipmentSwitchAction based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("switchEquipment", 2),
          ("allowSwitchToProtection", 3),
          ("allowSwitchToWorking", 4),
          ("inhibitSwitchToProtection", 5),
          ("inhibitSwitchToWorking", 6),
          ("switchTrafficToProtectionManual", 7),
          ("switchTrafficToWorkingManual", 8),
          ("switchTrafficToProtectionForce", 9),
          ("switchTrafficToWorkingForce", 10))
    )


_S300EquipmentSwitchAction_Type.__name__ = "Integer32"
_S300EquipmentSwitchAction_Object = MibTableColumn
s300EquipmentSwitchAction = _S300EquipmentSwitchAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 3, 1, 3),
    _S300EquipmentSwitchAction_Type()
)
s300EquipmentSwitchAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300EquipmentSwitchAction.setStatus("current")


class _S300EquipmentSwitchStatus_Type(Integer32):
    """Custom type s300EquipmentSwitchStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("manualPending", 2),
          ("forcePending", 3),
          ("forceComplete", 4),
          ("lockComplete", 5),
          ("autoPending", 6),
          ("autoComplete", 7),
          ("autoWaitToRestore", 8),
          ("manualComplete", 9),
          ("manualFail", 10),
          ("forceFail", 11),
          ("lockPending", 12),
          ("lockFail", 13),
          ("autoFail", 14),
          ("autoLock", 15),
          ("testPending", 16),
          ("testComplete", 17))
    )


_S300EquipmentSwitchStatus_Type.__name__ = "Integer32"
_S300EquipmentSwitchStatus_Object = MibTableColumn
s300EquipmentSwitchStatus = _S300EquipmentSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 3, 1, 4),
    _S300EquipmentSwitchStatus_Type()
)
s300EquipmentSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300EquipmentSwitchStatus.setStatus("current")


class _S300EquipmentProtectionStatus_Type(Integer32):
    """Custom type s300EquipmentProtectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("synching", 1),
          ("protectionAvailable", 2),
          ("protectionNotAvailable", 3))
    )


_S300EquipmentProtectionStatus_Type.__name__ = "Integer32"
_S300EquipmentProtectionStatus_Object = MibTableColumn
s300EquipmentProtectionStatus = _S300EquipmentProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 3, 1, 5),
    _S300EquipmentProtectionStatus_Type()
)
s300EquipmentProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300EquipmentProtectionStatus.setStatus("current")
_S300SoftwareTable_Object = MibTable
s300SoftwareTable = _S300SoftwareTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    s300SoftwareTable.setStatus("current")
_S300SoftwareEntry_Object = MibTableRow
s300SoftwareEntry = _S300SoftwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1)
)
s300SoftwareEntry.setIndexNames(
    (0, "Zhone", "zhoneShelfIndex"),
    (0, "Zhone", "zhoneSlotIndex"),
    (0, "ZHONE-SECHTOR300-MIB", "s300SoftwareBankNumber"),
)
if mibBuilder.loadTexts:
    s300SoftwareEntry.setStatus("current")


class _S300SoftwareBankNumber_Type(Integer32):
    """Custom type s300SoftwareBankNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_S300SoftwareBankNumber_Type.__name__ = "Integer32"
_S300SoftwareBankNumber_Object = MibTableColumn
s300SoftwareBankNumber = _S300SoftwareBankNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 1),
    _S300SoftwareBankNumber_Type()
)
s300SoftwareBankNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300SoftwareBankNumber.setStatus("current")
_S300SoftwareLoadName_Type = ZhoneAdminString
_S300SoftwareLoadName_Object = MibTableColumn
s300SoftwareLoadName = _S300SoftwareLoadName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 2),
    _S300SoftwareLoadName_Type()
)
s300SoftwareLoadName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300SoftwareLoadName.setStatus("current")
_S300SoftwareBootName_Type = ZhoneAdminString
_S300SoftwareBootName_Object = MibTableColumn
s300SoftwareBootName = _S300SoftwareBootName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 3),
    _S300SoftwareBootName_Type()
)
s300SoftwareBootName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300SoftwareBootName.setStatus("current")
_S300SoftwareFpga1Name_Type = ZhoneAdminString
_S300SoftwareFpga1Name_Object = MibTableColumn
s300SoftwareFpga1Name = _S300SoftwareFpga1Name_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 4),
    _S300SoftwareFpga1Name_Type()
)
s300SoftwareFpga1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300SoftwareFpga1Name.setStatus("current")
_S300SoftwareFpga2Name_Type = ZhoneAdminString
_S300SoftwareFpga2Name_Object = MibTableColumn
s300SoftwareFpga2Name = _S300SoftwareFpga2Name_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 5),
    _S300SoftwareFpga2Name_Type()
)
s300SoftwareFpga2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300SoftwareFpga2Name.setStatus("current")
_S300SoftwareCpldName_Type = ZhoneAdminString
_S300SoftwareCpldName_Object = MibTableColumn
s300SoftwareCpldName = _S300SoftwareCpldName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 6),
    _S300SoftwareCpldName_Type()
)
s300SoftwareCpldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300SoftwareCpldName.setStatus("current")
_S300SoftwareBspName_Type = ZhoneAdminString
_S300SoftwareBspName_Object = MibTableColumn
s300SoftwareBspName = _S300SoftwareBspName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 7),
    _S300SoftwareBspName_Type()
)
s300SoftwareBspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300SoftwareBspName.setStatus("current")


class _S300SoftwareBankStatus_Type(Integer32):
    """Custom type s300SoftwareBankStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("loadInProgress", 3),
          ("bankChecksumError", 4),
          ("empty", 5))
    )


_S300SoftwareBankStatus_Type.__name__ = "Integer32"
_S300SoftwareBankStatus_Object = MibTableColumn
s300SoftwareBankStatus = _S300SoftwareBankStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 4, 1, 8),
    _S300SoftwareBankStatus_Type()
)
s300SoftwareBankStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300SoftwareBankStatus.setStatus("current")
_S300EquipmentTraps_ObjectIdentity = ObjectIdentity
s300EquipmentTraps = _S300EquipmentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 5)
)
if mibBuilder.loadTexts:
    s300EquipmentTraps.setStatus("current")
_S300EquipmentV2Traps_ObjectIdentity = ObjectIdentity
s300EquipmentV2Traps = _S300EquipmentV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 5, 0)
)
if mibBuilder.loadTexts:
    s300EquipmentV2Traps.setStatus("current")
_S300Dsx_ObjectIdentity = ObjectIdentity
s300Dsx = _S300Dsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    s300Dsx.setStatus("current")
_S300TdmXcon_ObjectIdentity = ObjectIdentity
s300TdmXcon = _S300TdmXcon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    s300TdmXcon.setStatus("current")


class _S300NextTpId_Type(Integer32):
    """Custom type s300NextTpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300NextTpId_Type.__name__ = "Integer32"
_S300NextTpId_Object = MibScalar
s300NextTpId = _S300NextTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 1),
    _S300NextTpId_Type()
)
s300NextTpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300NextTpId.setStatus("current")


class _S300NextCrsId_Type(Integer32):
    """Custom type s300NextCrsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300NextCrsId_Type.__name__ = "Integer32"
_S300NextCrsId_Object = MibScalar
s300NextCrsId = _S300NextCrsId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 2),
    _S300NextCrsId_Type()
)
s300NextCrsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300NextCrsId.setStatus("current")
_S300TpTable_Object = MibTable
s300TpTable = _S300TpTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    s300TpTable.setStatus("current")
_S300TpEntry_Object = MibTableRow
s300TpEntry = _S300TpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1)
)
s300TpEntry.setIndexNames(
    (0, "ZHONE-SECHTOR300-MIB", "s300TpId"),
)
if mibBuilder.loadTexts:
    s300TpEntry.setStatus("current")


class _S300TpId_Type(Integer32):
    """Custom type s300TpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300TpId_Type.__name__ = "Integer32"
_S300TpId_Object = MibTableColumn
s300TpId = _S300TpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 1),
    _S300TpId_Type()
)
s300TpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300TpId.setStatus("current")


class _S300TsMap_Type(Bits):
    """Custom type s300TsMap based on Bits"""
    namedValues = NamedValues(
        *(("timeslot1", 0),
          ("timeslot2", 1),
          ("timeslot3", 2),
          ("timeslot4", 3),
          ("timeslot5", 4),
          ("timeslot6", 5),
          ("timeslot7", 6),
          ("timeslot8", 7),
          ("timeslot9", 8),
          ("timeslot10", 9),
          ("timeslot11", 10),
          ("timeslot12", 11),
          ("timeslot13", 12),
          ("timeslot14", 13),
          ("timeslot15", 14),
          ("timeslot16", 15),
          ("timeslot17", 16),
          ("timeslot18", 17),
          ("timeslot19", 18),
          ("timeslot20", 19),
          ("timeslot21", 20),
          ("timeslot22", 21),
          ("timeslot23", 22),
          ("timeslot24", 23),
          ("timeslot25", 24),
          ("timeslot26", 25),
          ("timeslot27", 26),
          ("timeslot28", 27),
          ("timeslot29", 28),
          ("timeslot30", 29),
          ("timeslot31", 30),
          ("timeslot32", 31))
    )

_S300TsMap_Type.__name__ = "Bits"
_S300TsMap_Object = MibTableColumn
s300TsMap = _S300TsMap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 2),
    _S300TsMap_Type()
)
s300TsMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TsMap.setStatus("current")
_S300TpIfIndex_Type = InterfaceIndex
_S300TpIfIndex_Object = MibTableColumn
s300TpIfIndex = _S300TpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 3),
    _S300TpIfIndex_Type()
)
s300TpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpIfIndex.setStatus("current")


class _S300TpTrafficType_Type(Integer32):
    """Custom type s300TpTrafficType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("voice", 1),
          ("vsig", 2),
          ("data", 3))
    )


_S300TpTrafficType_Type.__name__ = "Integer32"
_S300TpTrafficType_Object = MibTableColumn
s300TpTrafficType = _S300TpTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 4),
    _S300TpTrafficType_Type()
)
s300TpTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpTrafficType.setStatus("current")


class _S300TpType_Type(Integer32):
    """Custom type s300TpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("staticXconTP", 1),
          ("ipTP", 2),
          ("alrTP", 3),
          ("ds1lrTP", 4),
          ("busTP", 5))
    )


_S300TpType_Type.__name__ = "Integer32"
_S300TpType_Object = MibTableColumn
s300TpType = _S300TpType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 5),
    _S300TpType_Type()
)
s300TpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpType.setStatus("current")
_S300TpTcABCD1_Type = ZhoneABCDValue
_S300TpTcABCD1_Object = MibTableColumn
s300TpTcABCD1 = _S300TpTcABCD1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 6),
    _S300TpTcABCD1_Type()
)
s300TpTcABCD1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpTcABCD1.setStatus("current")
_S300TpTcABCD2_Type = ZhoneABCDValue
_S300TpTcABCD2_Object = MibTableColumn
s300TpTcABCD2 = _S300TpTcABCD2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 7),
    _S300TpTcABCD2_Type()
)
s300TpTcABCD2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpTcABCD2.setStatus("current")


class _S300TpSigCnv_Type(Integer32):
    """Custom type s300TpSigCnv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("txRx", 2),
          ("tx", 3),
          ("rx", 4))
    )


_S300TpSigCnv_Type.__name__ = "Integer32"
_S300TpSigCnv_Object = MibTableColumn
s300TpSigCnv = _S300TpSigCnv_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 8),
    _S300TpSigCnv_Type()
)
s300TpSigCnv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpSigCnv.setStatus("current")
_S300TpSigConversionRxId_Type = ZhoneAdminString
_S300TpSigConversionRxId_Object = MibTableColumn
s300TpSigConversionRxId = _S300TpSigConversionRxId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 9),
    _S300TpSigConversionRxId_Type()
)
s300TpSigConversionRxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300TpSigConversionRxId.setStatus("current")
_S300TpSigConversionTxId_Type = ZhoneAdminString
_S300TpSigConversionTxId_Object = MibTableColumn
s300TpSigConversionTxId = _S300TpSigConversionTxId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 10),
    _S300TpSigConversionTxId_Type()
)
s300TpSigConversionTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300TpSigConversionTxId.setStatus("current")


class _S300TpDiag_Type(TruthValue):
    """Custom type s300TpDiag based on TruthValue"""
    defaultValue = 2


_S300TpDiag_Type.__name__ = "TruthValue"
_S300TpDiag_Object = MibTableColumn
s300TpDiag = _S300TpDiag_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 11),
    _S300TpDiag_Type()
)
s300TpDiag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpDiag.setStatus("current")


class _S300TpCrsId_Type(Integer32):
    """Custom type s300TpCrsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_S300TpCrsId_Type.__name__ = "Integer32"
_S300TpCrsId_Object = MibTableColumn
s300TpCrsId = _S300TpCrsId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 12),
    _S300TpCrsId_Type()
)
s300TpCrsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300TpCrsId.setStatus("current")
_S300TpRowStatus_Type = ZhoneRowStatus
_S300TpRowStatus_Object = MibTableColumn
s300TpRowStatus = _S300TpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 3, 1, 13),
    _S300TpRowStatus_Type()
)
s300TpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300TpRowStatus.setStatus("current")
_S300CrsTable_Object = MibTable
s300CrsTable = _S300CrsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    s300CrsTable.setStatus("current")
_S300CrsEntry_Object = MibTableRow
s300CrsEntry = _S300CrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4, 1)
)
s300CrsEntry.setIndexNames(
    (0, "ZHONE-SECHTOR300-MIB", "s300CrsId"),
)
if mibBuilder.loadTexts:
    s300CrsEntry.setStatus("current")


class _S300CrsId_Type(Integer32):
    """Custom type s300CrsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300CrsId_Type.__name__ = "Integer32"
_S300CrsId_Object = MibTableColumn
s300CrsId = _S300CrsId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4, 1, 1),
    _S300CrsId_Type()
)
s300CrsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300CrsId.setStatus("current")


class _S300CrsPrimaryTpId_Type(Integer32):
    """Custom type s300CrsPrimaryTpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300CrsPrimaryTpId_Type.__name__ = "Integer32"
_S300CrsPrimaryTpId_Object = MibTableColumn
s300CrsPrimaryTpId = _S300CrsPrimaryTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4, 1, 2),
    _S300CrsPrimaryTpId_Type()
)
s300CrsPrimaryTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300CrsPrimaryTpId.setStatus("current")


class _S300CrsBidirectionalTpId_Type(Integer32):
    """Custom type s300CrsBidirectionalTpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300CrsBidirectionalTpId_Type.__name__ = "Integer32"
_S300CrsBidirectionalTpId_Object = MibTableColumn
s300CrsBidirectionalTpId = _S300CrsBidirectionalTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4, 1, 3),
    _S300CrsBidirectionalTpId_Type()
)
s300CrsBidirectionalTpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300CrsBidirectionalTpId.setStatus("current")


class _S300CrsName_Type(ZhoneAdminString):
    """Custom type s300CrsName based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_S300CrsName_Type.__name__ = "ZhoneAdminString"
_S300CrsName_Object = MibTableColumn
s300CrsName = _S300CrsName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4, 1, 4),
    _S300CrsName_Type()
)
s300CrsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300CrsName.setStatus("current")


class _S300CrsType_Type(Integer32):
    """Custom type s300CrsType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemCrs", 1),
          ("userCrs", 2))
    )


_S300CrsType_Type.__name__ = "Integer32"
_S300CrsType_Object = MibTableColumn
s300CrsType = _S300CrsType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4, 1, 5),
    _S300CrsType_Type()
)
s300CrsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300CrsType.setStatus("current")
_S300CrsRowStatus_Type = ZhoneRowStatus
_S300CrsRowStatus_Object = MibTableColumn
s300CrsRowStatus = _S300CrsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 4, 1, 6),
    _S300CrsRowStatus_Type()
)
s300CrsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300CrsRowStatus.setStatus("current")
_S300CrsBroadcastTable_Object = MibTable
s300CrsBroadcastTable = _S300CrsBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    s300CrsBroadcastTable.setStatus("current")
_S300CrsBroadcastEntry_Object = MibTableRow
s300CrsBroadcastEntry = _S300CrsBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 5, 1)
)
s300CrsBroadcastEntry.setIndexNames(
    (0, "ZHONE-SECHTOR300-MIB", "s300CrsId"),
    (0, "ZHONE-SECHTOR300-MIB", "s300TpId"),
)
if mibBuilder.loadTexts:
    s300CrsBroadcastEntry.setStatus("current")
_S300CrsUniLeafRowStatus_Type = ZhoneRowStatus
_S300CrsUniLeafRowStatus_Object = MibTableColumn
s300CrsUniLeafRowStatus = _S300CrsUniLeafRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 1, 5, 1, 1),
    _S300CrsUniLeafRowStatus_Type()
)
s300CrsUniLeafRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300CrsUniLeafRowStatus.setStatus("current")
_S300Bert_ObjectIdentity = ObjectIdentity
s300Bert = _S300Bert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    s300Bert.setStatus("current")
_S300BertTable_Object = MibTable
s300BertTable = _S300BertTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    s300BertTable.setStatus("current")
_S300BertEntry_Object = MibTableRow
s300BertEntry = _S300BertEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    s300BertEntry.setStatus("current")


class _S300BertType_Type(Integer32):
    """Custom type s300BertType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("space", 2),
          ("mark", 3),
          ("qrss", 4))
    )


_S300BertType_Type.__name__ = "Integer32"
_S300BertType_Object = MibTableColumn
s300BertType = _S300BertType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 1),
    _S300BertType_Type()
)
s300BertType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300BertType.setStatus("current")


class _S300BertAdmin_Type(Integer32):
    """Custom type s300BertAdmin based on Integer32"""
    defaultValue = 2

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


_S300BertAdmin_Type.__name__ = "Integer32"
_S300BertAdmin_Object = MibTableColumn
s300BertAdmin = _S300BertAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 2),
    _S300BertAdmin_Type()
)
s300BertAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300BertAdmin.setStatus("current")


class _S300BertInsertBitError_Type(TruthValue):
    """Custom type s300BertInsertBitError based on TruthValue"""
    defaultValue = 2


_S300BertInsertBitError_Type.__name__ = "TruthValue"
_S300BertInsertBitError_Object = MibTableColumn
s300BertInsertBitError = _S300BertInsertBitError_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 3),
    _S300BertInsertBitError_Type()
)
s300BertInsertBitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300BertInsertBitError.setStatus("current")
_S300BertElaspedTime_Type = TimeTicks
_S300BertElaspedTime_Object = MibTableColumn
s300BertElaspedTime = _S300BertElaspedTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 4),
    _S300BertElaspedTime_Type()
)
s300BertElaspedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300BertElaspedTime.setStatus("current")


class _S300BertSeverelyErroredSeconds_Type(Integer32):
    """Custom type s300BertSeverelyErroredSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300BertSeverelyErroredSeconds_Type.__name__ = "Integer32"
_S300BertSeverelyErroredSeconds_Object = MibTableColumn
s300BertSeverelyErroredSeconds = _S300BertSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 5),
    _S300BertSeverelyErroredSeconds_Type()
)
s300BertSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300BertSeverelyErroredSeconds.setStatus("current")


class _S300BertOutOfSynchSeconds_Type(Integer32):
    """Custom type s300BertOutOfSynchSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300BertOutOfSynchSeconds_Type.__name__ = "Integer32"
_S300BertOutOfSynchSeconds_Object = MibTableColumn
s300BertOutOfSynchSeconds = _S300BertOutOfSynchSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 6),
    _S300BertOutOfSynchSeconds_Type()
)
s300BertOutOfSynchSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300BertOutOfSynchSeconds.setStatus("current")
_S300BertBitErrorRate_Type = OctetString
_S300BertBitErrorRate_Object = MibTableColumn
s300BertBitErrorRate = _S300BertBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 7),
    _S300BertBitErrorRate_Type()
)
s300BertBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300BertBitErrorRate.setStatus("current")


class _S300BertClearStats_Type(TruthValue):
    """Custom type s300BertClearStats based on TruthValue"""
    defaultValue = 2


_S300BertClearStats_Type.__name__ = "TruthValue"
_S300BertClearStats_Object = MibTableColumn
s300BertClearStats = _S300BertClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 2, 1, 1, 8),
    _S300BertClearStats_Type()
)
s300BertClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300BertClearStats.setStatus("current")
_S300Ds1_ObjectIdentity = ObjectIdentity
s300Ds1 = _S300Ds1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    s300Ds1.setStatus("current")
_S300Ds1Table_Object = MibTable
s300Ds1Table = _S300Ds1Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    s300Ds1Table.setStatus("current")
_S300Ds1Entry_Object = MibTableRow
s300Ds1Entry = _S300Ds1Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    s300Ds1Entry.setStatus("current")


class _S300Ds1OtherFdlType_Type(Integer32):
    """Custom type s300Ds1OtherFdlType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("slc96Note", 1),
          ("slc96Wp1", 2),
          ("slc96Wp1b", 3),
          ("none", 4))
    )


_S300Ds1OtherFdlType_Type.__name__ = "Integer32"
_S300Ds1OtherFdlType_Object = MibTableColumn
s300Ds1OtherFdlType = _S300Ds1OtherFdlType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 1),
    _S300Ds1OtherFdlType_Type()
)
s300Ds1OtherFdlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds1OtherFdlType.setStatus("current")


class _S300Ds1FarEndLoopbackConfig_Type(Integer32):
    """Custom type s300Ds1FarEndLoopbackConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("timeout", 3))
    )


_S300Ds1FarEndLoopbackConfig_Type.__name__ = "Integer32"
_S300Ds1FarEndLoopbackConfig_Object = MibTableColumn
s300Ds1FarEndLoopbackConfig = _S300Ds1FarEndLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 2),
    _S300Ds1FarEndLoopbackConfig_Type()
)
s300Ds1FarEndLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds1FarEndLoopbackConfig.setStatus("current")


class _S300Ds1FarEndLoopbackCtrl_Type(Integer32):
    """Custom type s300Ds1FarEndLoopbackCtrl based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("farEndLine", 1),
          ("farEndPayload", 2),
          ("farEndCsu", 3),
          ("none", 4))
    )


_S300Ds1FarEndLoopbackCtrl_Type.__name__ = "Integer32"
_S300Ds1FarEndLoopbackCtrl_Object = MibTableColumn
s300Ds1FarEndLoopbackCtrl = _S300Ds1FarEndLoopbackCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 3),
    _S300Ds1FarEndLoopbackCtrl_Type()
)
s300Ds1FarEndLoopbackCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds1FarEndLoopbackCtrl.setStatus("current")


class _S300Ds1Conversion_Type(Integer32):
    """Custom type s300Ds1Conversion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pcmAlawToUlawRX", 2),
          ("pcmAlawToUlawTX", 3),
          ("pcmAlawToUlawTXRX", 4),
          ("sigRX", 5),
          ("sigTX", 6),
          ("sigTXRX", 7))
    )


_S300Ds1Conversion_Type.__name__ = "Integer32"
_S300Ds1Conversion_Object = MibTableColumn
s300Ds1Conversion = _S300Ds1Conversion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 4),
    _S300Ds1Conversion_Type()
)
s300Ds1Conversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds1Conversion.setStatus("current")
_S300Ds1SigConversionRxId_Type = ZhoneAdminString
_S300Ds1SigConversionRxId_Object = MibTableColumn
s300Ds1SigConversionRxId = _S300Ds1SigConversionRxId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 5),
    _S300Ds1SigConversionRxId_Type()
)
s300Ds1SigConversionRxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300Ds1SigConversionRxId.setStatus("current")
_S300Ds1SigConversionTxId_Type = ZhoneAdminString
_S300Ds1SigConversionTxId_Object = MibTableColumn
s300Ds1SigConversionTxId = _S300Ds1SigConversionTxId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 6),
    _S300Ds1SigConversionTxId_Type()
)
s300Ds1SigConversionTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300Ds1SigConversionTxId.setStatus("current")


class _S300Ds1LineBuildOut_Type(Integer32):
    """Custom type s300Ds1LineBuildOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("lineBuildOut0", 2),
          ("lineBuildOut7p5", 3),
          ("lineBuildOut15", 4),
          ("lineBuildOut22p5", 5))
    )


_S300Ds1LineBuildOut_Type.__name__ = "Integer32"
_S300Ds1LineBuildOut_Object = MibTableColumn
s300Ds1LineBuildOut = _S300Ds1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 7),
    _S300Ds1LineBuildOut_Type()
)
s300Ds1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds1LineBuildOut.setStatus("current")


class _S300Ds1ConnectorType_Type(Integer32):
    """Custom type s300Ds1ConnectorType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("connector75ohm", 2),
          ("connector120ohm", 3))
    )


_S300Ds1ConnectorType_Type.__name__ = "Integer32"
_S300Ds1ConnectorType_Object = MibTableColumn
s300Ds1ConnectorType = _S300Ds1ConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 3, 1, 1, 8),
    _S300Ds1ConnectorType_Type()
)
s300Ds1ConnectorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds1ConnectorType.setStatus("current")
_S300SigConversion_ObjectIdentity = ObjectIdentity
s300SigConversion = _S300SigConversion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4)
)
if mibBuilder.loadTexts:
    s300SigConversion.setStatus("current")
_S300SigConversionRxTable_Object = MibTable
s300SigConversionRxTable = _S300SigConversionRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    s300SigConversionRxTable.setStatus("current")
_S300SigConversionRxEntry_Object = MibTableRow
s300SigConversionRxEntry = _S300SigConversionRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1)
)
s300SigConversionRxEntry.setIndexNames(
    (1, "ZHONE-SECHTOR300-MIB", "sigConversionRxIdentification"),
)
if mibBuilder.loadTexts:
    s300SigConversionRxEntry.setStatus("current")


class _SigConversionRxIdentification_Type(ZhoneAdminString):
    """Custom type sigConversionRxIdentification based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SigConversionRxIdentification_Type.__name__ = "ZhoneAdminString"
_SigConversionRxIdentification_Object = MibTableColumn
sigConversionRxIdentification = _SigConversionRxIdentification_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 1),
    _SigConversionRxIdentification_Type()
)
sigConversionRxIdentification.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigConversionRxIdentification.setStatus("current")


class _SigRx0000_Type(ZhoneABCDValue):
    """Custom type sigRx0000 based on ZhoneABCDValue"""
    defaultValue = 1


_SigRx0000_Type.__name__ = "ZhoneABCDValue"
_SigRx0000_Object = MibTableColumn
sigRx0000 = _SigRx0000_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 2),
    _SigRx0000_Type()
)
sigRx0000.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0000.setStatus("current")


class _SigRx0001_Type(ZhoneABCDValue):
    """Custom type sigRx0001 based on ZhoneABCDValue"""
    defaultValue = 2


_SigRx0001_Type.__name__ = "ZhoneABCDValue"
_SigRx0001_Object = MibTableColumn
sigRx0001 = _SigRx0001_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 3),
    _SigRx0001_Type()
)
sigRx0001.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0001.setStatus("current")


class _SigRx0010_Type(ZhoneABCDValue):
    """Custom type sigRx0010 based on ZhoneABCDValue"""
    defaultValue = 3


_SigRx0010_Type.__name__ = "ZhoneABCDValue"
_SigRx0010_Object = MibTableColumn
sigRx0010 = _SigRx0010_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 4),
    _SigRx0010_Type()
)
sigRx0010.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0010.setStatus("current")


class _SigRx0011_Type(ZhoneABCDValue):
    """Custom type sigRx0011 based on ZhoneABCDValue"""
    defaultValue = 4


_SigRx0011_Type.__name__ = "ZhoneABCDValue"
_SigRx0011_Object = MibTableColumn
sigRx0011 = _SigRx0011_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 5),
    _SigRx0011_Type()
)
sigRx0011.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0011.setStatus("current")


class _SigRx0100_Type(ZhoneABCDValue):
    """Custom type sigRx0100 based on ZhoneABCDValue"""
    defaultValue = 5


_SigRx0100_Type.__name__ = "ZhoneABCDValue"
_SigRx0100_Object = MibTableColumn
sigRx0100 = _SigRx0100_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 6),
    _SigRx0100_Type()
)
sigRx0100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0100.setStatus("current")


class _SigRx0101_Type(ZhoneABCDValue):
    """Custom type sigRx0101 based on ZhoneABCDValue"""
    defaultValue = 6


_SigRx0101_Type.__name__ = "ZhoneABCDValue"
_SigRx0101_Object = MibTableColumn
sigRx0101 = _SigRx0101_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 7),
    _SigRx0101_Type()
)
sigRx0101.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0101.setStatus("current")


class _SigRx0110_Type(ZhoneABCDValue):
    """Custom type sigRx0110 based on ZhoneABCDValue"""
    defaultValue = 7


_SigRx0110_Type.__name__ = "ZhoneABCDValue"
_SigRx0110_Object = MibTableColumn
sigRx0110 = _SigRx0110_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 8),
    _SigRx0110_Type()
)
sigRx0110.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0110.setStatus("current")


class _SigRx0111_Type(ZhoneABCDValue):
    """Custom type sigRx0111 based on ZhoneABCDValue"""
    defaultValue = 8


_SigRx0111_Type.__name__ = "ZhoneABCDValue"
_SigRx0111_Object = MibTableColumn
sigRx0111 = _SigRx0111_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 9),
    _SigRx0111_Type()
)
sigRx0111.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx0111.setStatus("current")


class _SigRx1000_Type(ZhoneABCDValue):
    """Custom type sigRx1000 based on ZhoneABCDValue"""
    defaultValue = 9


_SigRx1000_Type.__name__ = "ZhoneABCDValue"
_SigRx1000_Object = MibTableColumn
sigRx1000 = _SigRx1000_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 10),
    _SigRx1000_Type()
)
sigRx1000.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1000.setStatus("current")


class _SigRx1001_Type(ZhoneABCDValue):
    """Custom type sigRx1001 based on ZhoneABCDValue"""
    defaultValue = 10


_SigRx1001_Type.__name__ = "ZhoneABCDValue"
_SigRx1001_Object = MibTableColumn
sigRx1001 = _SigRx1001_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 11),
    _SigRx1001_Type()
)
sigRx1001.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1001.setStatus("current")


class _SigRx1010_Type(ZhoneABCDValue):
    """Custom type sigRx1010 based on ZhoneABCDValue"""
    defaultValue = 11


_SigRx1010_Type.__name__ = "ZhoneABCDValue"
_SigRx1010_Object = MibTableColumn
sigRx1010 = _SigRx1010_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 12),
    _SigRx1010_Type()
)
sigRx1010.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1010.setStatus("current")


class _SigRx1011_Type(ZhoneABCDValue):
    """Custom type sigRx1011 based on ZhoneABCDValue"""
    defaultValue = 12


_SigRx1011_Type.__name__ = "ZhoneABCDValue"
_SigRx1011_Object = MibTableColumn
sigRx1011 = _SigRx1011_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 13),
    _SigRx1011_Type()
)
sigRx1011.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1011.setStatus("current")


class _SigRx1100_Type(ZhoneABCDValue):
    """Custom type sigRx1100 based on ZhoneABCDValue"""
    defaultValue = 13


_SigRx1100_Type.__name__ = "ZhoneABCDValue"
_SigRx1100_Object = MibTableColumn
sigRx1100 = _SigRx1100_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 14),
    _SigRx1100_Type()
)
sigRx1100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1100.setStatus("current")


class _SigRx1101_Type(ZhoneABCDValue):
    """Custom type sigRx1101 based on ZhoneABCDValue"""
    defaultValue = 14


_SigRx1101_Type.__name__ = "ZhoneABCDValue"
_SigRx1101_Object = MibTableColumn
sigRx1101 = _SigRx1101_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 15),
    _SigRx1101_Type()
)
sigRx1101.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1101.setStatus("current")


class _SigRx1110_Type(ZhoneABCDValue):
    """Custom type sigRx1110 based on ZhoneABCDValue"""
    defaultValue = 15


_SigRx1110_Type.__name__ = "ZhoneABCDValue"
_SigRx1110_Object = MibTableColumn
sigRx1110 = _SigRx1110_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 16),
    _SigRx1110_Type()
)
sigRx1110.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1110.setStatus("current")


class _SigRx1111_Type(ZhoneABCDValue):
    """Custom type sigRx1111 based on ZhoneABCDValue"""
    defaultValue = 16


_SigRx1111_Type.__name__ = "ZhoneABCDValue"
_SigRx1111_Object = MibTableColumn
sigRx1111 = _SigRx1111_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 1, 1, 17),
    _SigRx1111_Type()
)
sigRx1111.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigRx1111.setStatus("current")
_S300SigConversionTxTable_Object = MibTable
s300SigConversionTxTable = _S300SigConversionTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    s300SigConversionTxTable.setStatus("current")
_S300SigConversionTxEntry_Object = MibTableRow
s300SigConversionTxEntry = _S300SigConversionTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1)
)
s300SigConversionTxEntry.setIndexNames(
    (1, "ZHONE-SECHTOR300-MIB", "sigConversionTxIdentification"),
)
if mibBuilder.loadTexts:
    s300SigConversionTxEntry.setStatus("current")


class _SigConversionTxIdentification_Type(ZhoneAdminString):
    """Custom type sigConversionTxIdentification based on ZhoneAdminString"""
    subtypeSpec = ZhoneAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SigConversionTxIdentification_Type.__name__ = "ZhoneAdminString"
_SigConversionTxIdentification_Object = MibTableColumn
sigConversionTxIdentification = _SigConversionTxIdentification_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 1),
    _SigConversionTxIdentification_Type()
)
sigConversionTxIdentification.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sigConversionTxIdentification.setStatus("current")


class _SigTx0000_Type(ZhoneABCDValue):
    """Custom type sigTx0000 based on ZhoneABCDValue"""
    defaultValue = 1


_SigTx0000_Type.__name__ = "ZhoneABCDValue"
_SigTx0000_Object = MibTableColumn
sigTx0000 = _SigTx0000_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 2),
    _SigTx0000_Type()
)
sigTx0000.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0000.setStatus("current")


class _SigTx0001_Type(ZhoneABCDValue):
    """Custom type sigTx0001 based on ZhoneABCDValue"""
    defaultValue = 2


_SigTx0001_Type.__name__ = "ZhoneABCDValue"
_SigTx0001_Object = MibTableColumn
sigTx0001 = _SigTx0001_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 3),
    _SigTx0001_Type()
)
sigTx0001.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0001.setStatus("current")


class _SigTx0010_Type(ZhoneABCDValue):
    """Custom type sigTx0010 based on ZhoneABCDValue"""
    defaultValue = 3


_SigTx0010_Type.__name__ = "ZhoneABCDValue"
_SigTx0010_Object = MibTableColumn
sigTx0010 = _SigTx0010_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 4),
    _SigTx0010_Type()
)
sigTx0010.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0010.setStatus("current")


class _SigTx0011_Type(ZhoneABCDValue):
    """Custom type sigTx0011 based on ZhoneABCDValue"""
    defaultValue = 4


_SigTx0011_Type.__name__ = "ZhoneABCDValue"
_SigTx0011_Object = MibTableColumn
sigTx0011 = _SigTx0011_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 5),
    _SigTx0011_Type()
)
sigTx0011.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0011.setStatus("current")


class _SigTx0100_Type(ZhoneABCDValue):
    """Custom type sigTx0100 based on ZhoneABCDValue"""
    defaultValue = 5


_SigTx0100_Type.__name__ = "ZhoneABCDValue"
_SigTx0100_Object = MibTableColumn
sigTx0100 = _SigTx0100_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 6),
    _SigTx0100_Type()
)
sigTx0100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0100.setStatus("current")


class _SigTx0101_Type(ZhoneABCDValue):
    """Custom type sigTx0101 based on ZhoneABCDValue"""
    defaultValue = 6


_SigTx0101_Type.__name__ = "ZhoneABCDValue"
_SigTx0101_Object = MibTableColumn
sigTx0101 = _SigTx0101_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 7),
    _SigTx0101_Type()
)
sigTx0101.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0101.setStatus("current")


class _SigTx0110_Type(ZhoneABCDValue):
    """Custom type sigTx0110 based on ZhoneABCDValue"""
    defaultValue = 7


_SigTx0110_Type.__name__ = "ZhoneABCDValue"
_SigTx0110_Object = MibTableColumn
sigTx0110 = _SigTx0110_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 8),
    _SigTx0110_Type()
)
sigTx0110.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0110.setStatus("current")


class _SigTx0111_Type(ZhoneABCDValue):
    """Custom type sigTx0111 based on ZhoneABCDValue"""
    defaultValue = 8


_SigTx0111_Type.__name__ = "ZhoneABCDValue"
_SigTx0111_Object = MibTableColumn
sigTx0111 = _SigTx0111_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 9),
    _SigTx0111_Type()
)
sigTx0111.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx0111.setStatus("current")


class _SigTx1000_Type(ZhoneABCDValue):
    """Custom type sigTx1000 based on ZhoneABCDValue"""
    defaultValue = 9


_SigTx1000_Type.__name__ = "ZhoneABCDValue"
_SigTx1000_Object = MibTableColumn
sigTx1000 = _SigTx1000_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 10),
    _SigTx1000_Type()
)
sigTx1000.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1000.setStatus("current")


class _SigTx1001_Type(ZhoneABCDValue):
    """Custom type sigTx1001 based on ZhoneABCDValue"""
    defaultValue = 10


_SigTx1001_Type.__name__ = "ZhoneABCDValue"
_SigTx1001_Object = MibTableColumn
sigTx1001 = _SigTx1001_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 11),
    _SigTx1001_Type()
)
sigTx1001.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1001.setStatus("current")


class _SigTx1010_Type(ZhoneABCDValue):
    """Custom type sigTx1010 based on ZhoneABCDValue"""
    defaultValue = 11


_SigTx1010_Type.__name__ = "ZhoneABCDValue"
_SigTx1010_Object = MibTableColumn
sigTx1010 = _SigTx1010_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 12),
    _SigTx1010_Type()
)
sigTx1010.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1010.setStatus("current")


class _SigTx1011_Type(ZhoneABCDValue):
    """Custom type sigTx1011 based on ZhoneABCDValue"""
    defaultValue = 12


_SigTx1011_Type.__name__ = "ZhoneABCDValue"
_SigTx1011_Object = MibTableColumn
sigTx1011 = _SigTx1011_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 13),
    _SigTx1011_Type()
)
sigTx1011.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1011.setStatus("current")


class _SigTx1100_Type(ZhoneABCDValue):
    """Custom type sigTx1100 based on ZhoneABCDValue"""
    defaultValue = 13


_SigTx1100_Type.__name__ = "ZhoneABCDValue"
_SigTx1100_Object = MibTableColumn
sigTx1100 = _SigTx1100_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 14),
    _SigTx1100_Type()
)
sigTx1100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1100.setStatus("current")


class _SigTx1101_Type(ZhoneABCDValue):
    """Custom type sigTx1101 based on ZhoneABCDValue"""
    defaultValue = 14


_SigTx1101_Type.__name__ = "ZhoneABCDValue"
_SigTx1101_Object = MibTableColumn
sigTx1101 = _SigTx1101_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 15),
    _SigTx1101_Type()
)
sigTx1101.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1101.setStatus("current")


class _SigTx1110_Type(ZhoneABCDValue):
    """Custom type sigTx1110 based on ZhoneABCDValue"""
    defaultValue = 15


_SigTx1110_Type.__name__ = "ZhoneABCDValue"
_SigTx1110_Object = MibTableColumn
sigTx1110 = _SigTx1110_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 16),
    _SigTx1110_Type()
)
sigTx1110.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1110.setStatus("current")


class _SigTx1111_Type(ZhoneABCDValue):
    """Custom type sigTx1111 based on ZhoneABCDValue"""
    defaultValue = 16


_SigTx1111_Type.__name__ = "ZhoneABCDValue"
_SigTx1111_Object = MibTableColumn
sigTx1111 = _SigTx1111_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 4, 2, 1, 17),
    _SigTx1111_Type()
)
sigTx1111.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sigTx1111.setStatus("current")
_S300Ds3_ObjectIdentity = ObjectIdentity
s300Ds3 = _S300Ds3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5)
)
if mibBuilder.loadTexts:
    s300Ds3.setStatus("current")
_S300Ds3Table_Object = MibTable
s300Ds3Table = _S300Ds3Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    s300Ds3Table.setStatus("current")
_S300Ds3Entry_Object = MibTableRow
s300Ds3Entry = _S300Ds3Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    s300Ds3Entry.setStatus("current")


class _S300Ds3LineStatus_Type(Bits):
    """Custom type s300Ds3LineStatus based on Bits"""
    namedValues = NamedValues(
        *(("ds3FaultPerr", 0),
          ("ds3FaultFebe", 1))
    )

_S300Ds3LineStatus_Type.__name__ = "Bits"
_S300Ds3LineStatus_Object = MibTableColumn
s300Ds3LineStatus = _S300Ds3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 1, 1, 1),
    _S300Ds3LineStatus_Type()
)
s300Ds3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300Ds3LineStatus.setStatus("current")


class _S300Ds3AisTxFormat_Type(Integer32):
    """Custom type s300Ds3AisTxFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("normal", 1)
    )


_S300Ds3AisTxFormat_Type.__name__ = "Integer32"
_S300Ds3AisTxFormat_Object = MibTableColumn
s300Ds3AisTxFormat = _S300Ds3AisTxFormat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 1, 1, 2),
    _S300Ds3AisTxFormat_Type()
)
s300Ds3AisTxFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds3AisTxFormat.setStatus("current")


class _S300Ds3AisDetFormat_Type(Integer32):
    """Custom type s300Ds3AisDetFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("framed1010Pattern", 1),
          ("framed1111Pattern", 2),
          ("unframedAllOnes", 3))
    )


_S300Ds3AisDetFormat_Type.__name__ = "Integer32"
_S300Ds3AisDetFormat_Object = MibTableColumn
s300Ds3AisDetFormat = _S300Ds3AisDetFormat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 1, 1, 3),
    _S300Ds3AisDetFormat_Type()
)
s300Ds3AisDetFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds3AisDetFormat.setStatus("current")


class _S300Ds3LoopbackConfig_Type(Integer32):
    """Custom type s300Ds3LoopbackConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("liuLineLoopback", 2),
          ("liuLocalLoopback", 3))
    )


_S300Ds3LoopbackConfig_Type.__name__ = "Integer32"
_S300Ds3LoopbackConfig_Object = MibTableColumn
s300Ds3LoopbackConfig = _S300Ds3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 1, 1, 4),
    _S300Ds3LoopbackConfig_Type()
)
s300Ds3LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300Ds3LoopbackConfig.setStatus("current")
_S300Ds3Traps_ObjectIdentity = ObjectIdentity
s300Ds3Traps = _S300Ds3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 2)
)
if mibBuilder.loadTexts:
    s300Ds3Traps.setStatus("current")
_S300Ds3V2Traps_ObjectIdentity = ObjectIdentity
s300Ds3V2Traps = _S300Ds3V2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 2, 0)
)
if mibBuilder.loadTexts:
    s300Ds3V2Traps.setStatus("current")
_S300System_ObjectIdentity = ObjectIdentity
s300System = _S300System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    s300System.setStatus("current")
_S300FileTransfer_ObjectIdentity = ObjectIdentity
s300FileTransfer = _S300FileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    s300FileTransfer.setStatus("current")


class _S300FileTransferSlot_Type(Integer32):
    """Custom type s300FileTransferSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_S300FileTransferSlot_Type.__name__ = "Integer32"
_S300FileTransferSlot_Object = MibScalar
s300FileTransferSlot = _S300FileTransferSlot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 1),
    _S300FileTransferSlot_Type()
)
s300FileTransferSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferSlot.setStatus("current")


class _S300FileTransferBankNumber_Type(Integer32):
    """Custom type s300FileTransferBankNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_S300FileTransferBankNumber_Type.__name__ = "Integer32"
_S300FileTransferBankNumber_Object = MibScalar
s300FileTransferBankNumber = _S300FileTransferBankNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 2),
    _S300FileTransferBankNumber_Type()
)
s300FileTransferBankNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferBankNumber.setStatus("current")
_S300FileTransferServerAddress_Type = IpAddress
_S300FileTransferServerAddress_Object = MibScalar
s300FileTransferServerAddress = _S300FileTransferServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 3),
    _S300FileTransferServerAddress_Type()
)
s300FileTransferServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferServerAddress.setStatus("current")
_S300FileTransferRemoteFileName_Type = ZhoneAdminString
_S300FileTransferRemoteFileName_Object = MibScalar
s300FileTransferRemoteFileName = _S300FileTransferRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 4),
    _S300FileTransferRemoteFileName_Type()
)
s300FileTransferRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferRemoteFileName.setStatus("current")


class _S300FileTransferFileType_Type(Integer32):
    """Custom type s300FileTransferFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("softwareImage", 1),
          ("bootImage", 2),
          ("fpga1Image", 3),
          ("fpga2Image", 4),
          ("bspImage", 5),
          ("nvmImage", 6))
    )


_S300FileTransferFileType_Type.__name__ = "Integer32"
_S300FileTransferFileType_Object = MibScalar
s300FileTransferFileType = _S300FileTransferFileType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 5),
    _S300FileTransferFileType_Type()
)
s300FileTransferFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferFileType.setStatus("current")


class _S300FileTransferType_Type(Integer32):
    """Custom type s300FileTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_S300FileTransferType_Type.__name__ = "Integer32"
_S300FileTransferType_Object = MibScalar
s300FileTransferType = _S300FileTransferType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 6),
    _S300FileTransferType_Type()
)
s300FileTransferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferType.setStatus("current")


class _S300FileTransferAdmin_Type(Integer32):
    """Custom type s300FileTransferAdmin based on Integer32"""
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


_S300FileTransferAdmin_Type.__name__ = "Integer32"
_S300FileTransferAdmin_Object = MibScalar
s300FileTransferAdmin = _S300FileTransferAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 7),
    _S300FileTransferAdmin_Type()
)
s300FileTransferAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferAdmin.setStatus("current")


class _S300FileTransferStatus_Type(Integer32):
    """Custom type s300FileTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("notInProgress", 2),
          ("completedWithoutError", 3),
          ("completedWithError", 4))
    )


_S300FileTransferStatus_Type.__name__ = "Integer32"
_S300FileTransferStatus_Object = MibScalar
s300FileTransferStatus = _S300FileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 8),
    _S300FileTransferStatus_Type()
)
s300FileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300FileTransferStatus.setStatus("current")


class _S300FileTransferFault_Type(Integer32):
    """Custom type s300FileTransferFault based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noFileFound", 1),
          ("crcError", 2),
          ("accessViolation", 3),
          ("diskFull", 4),
          ("fileExists", 5),
          ("internalError", 6),
          ("connectionDropped", 7),
          ("cardFault", 8),
          ("flashActive", 9),
          ("localTimeout", 10))
    )


_S300FileTransferFault_Type.__name__ = "Integer32"
_S300FileTransferFault_Object = MibScalar
s300FileTransferFault = _S300FileTransferFault_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 1, 9),
    _S300FileTransferFault_Type()
)
s300FileTransferFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300FileTransferFault.setStatus("current")
_S300Nvm_ObjectIdentity = ObjectIdentity
s300Nvm = _S300Nvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    s300Nvm.setStatus("current")
_S300NvmInit_Type = Integer32
_S300NvmInit_Object = MibScalar
s300NvmInit = _S300NvmInit_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 2, 1),
    _S300NvmInit_Type()
)
s300NvmInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300NvmInit.setStatus("current")
_S300Timing_ObjectIdentity = ObjectIdentity
s300Timing = _S300Timing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3)
)
if mibBuilder.loadTexts:
    s300Timing.setStatus("current")
_S300TimingConfig_ObjectIdentity = ObjectIdentity
s300TimingConfig = _S300TimingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    s300TimingConfig.setStatus("current")


class _S300TimingClksrc1Type_Type(Integer32):
    """Custom type s300TimingClksrc1Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("facility", 2),
          ("bitsAT1", 3),
          ("bitsBT1", 4))
    )


_S300TimingClksrc1Type_Type.__name__ = "Integer32"
_S300TimingClksrc1Type_Object = MibScalar
s300TimingClksrc1Type = _S300TimingClksrc1Type_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 1),
    _S300TimingClksrc1Type_Type()
)
s300TimingClksrc1Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc1Type.setStatus("current")
_S300TimingClksrc1Ifindex_Type = InterfaceIndex
_S300TimingClksrc1Ifindex_Object = MibScalar
s300TimingClksrc1Ifindex = _S300TimingClksrc1Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 2),
    _S300TimingClksrc1Ifindex_Type()
)
s300TimingClksrc1Ifindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc1Ifindex.setStatus("current")


class _S300TimingClksrc2Type_Type(Integer32):
    """Custom type s300TimingClksrc2Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("facility", 2),
          ("bitsAT1", 3),
          ("bitsBT1", 4))
    )


_S300TimingClksrc2Type_Type.__name__ = "Integer32"
_S300TimingClksrc2Type_Object = MibScalar
s300TimingClksrc2Type = _S300TimingClksrc2Type_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 3),
    _S300TimingClksrc2Type_Type()
)
s300TimingClksrc2Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc2Type.setStatus("current")
_S300TimingClksrc2Ifindex_Type = InterfaceIndex
_S300TimingClksrc2Ifindex_Object = MibScalar
s300TimingClksrc2Ifindex = _S300TimingClksrc2Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 4),
    _S300TimingClksrc2Ifindex_Type()
)
s300TimingClksrc2Ifindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc2Ifindex.setStatus("current")


class _S300TimingClksrc3Type_Type(Integer32):
    """Custom type s300TimingClksrc3Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("facility", 2),
          ("bitsAT1", 3),
          ("bitsBT1", 4))
    )


_S300TimingClksrc3Type_Type.__name__ = "Integer32"
_S300TimingClksrc3Type_Object = MibScalar
s300TimingClksrc3Type = _S300TimingClksrc3Type_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 5),
    _S300TimingClksrc3Type_Type()
)
s300TimingClksrc3Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc3Type.setStatus("current")
_S300TimingClksrc3Ifindex_Type = InterfaceIndex
_S300TimingClksrc3Ifindex_Object = MibScalar
s300TimingClksrc3Ifindex = _S300TimingClksrc3Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 6),
    _S300TimingClksrc3Ifindex_Type()
)
s300TimingClksrc3Ifindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc3Ifindex.setStatus("current")


class _S300TimingClksrc4Type_Type(Integer32):
    """Custom type s300TimingClksrc4Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("facility", 2),
          ("bitsAT1", 3),
          ("bitsBT1", 4))
    )


_S300TimingClksrc4Type_Type.__name__ = "Integer32"
_S300TimingClksrc4Type_Object = MibScalar
s300TimingClksrc4Type = _S300TimingClksrc4Type_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 7),
    _S300TimingClksrc4Type_Type()
)
s300TimingClksrc4Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc4Type.setStatus("current")
_S300TimingClksrc4Ifindex_Type = InterfaceIndex
_S300TimingClksrc4Ifindex_Object = MibScalar
s300TimingClksrc4Ifindex = _S300TimingClksrc4Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 8),
    _S300TimingClksrc4Ifindex_Type()
)
s300TimingClksrc4Ifindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300TimingClksrc4Ifindex.setStatus("current")


class _S300TimingClksrcActiveClock_Type(Integer32):
    """Custom type s300TimingClksrcActiveClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clksrc1", 1),
          ("clksrc2", 2),
          ("clksrc3", 3),
          ("clksrc4", 4))
    )


_S300TimingClksrcActiveClock_Type.__name__ = "Integer32"
_S300TimingClksrcActiveClock_Object = MibScalar
s300TimingClksrcActiveClock = _S300TimingClksrcActiveClock_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 3, 1, 9),
    _S300TimingClksrcActiveClock_Type()
)
s300TimingClksrcActiveClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300TimingClksrcActiveClock.setStatus("current")
_S300Alarms_ObjectIdentity = ObjectIdentity
s300Alarms = _S300Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 4)
)
if mibBuilder.loadTexts:
    s300Alarms.setStatus("current")


class _S300AlarmAudibleAlarmCutoff_Type(Integer32):
    """Custom type s300AlarmAudibleAlarmCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_S300AlarmAudibleAlarmCutoff_Type.__name__ = "Integer32"
_S300AlarmAudibleAlarmCutoff_Object = MibScalar
s300AlarmAudibleAlarmCutoff = _S300AlarmAudibleAlarmCutoff_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 4, 1),
    _S300AlarmAudibleAlarmCutoff_Type()
)
s300AlarmAudibleAlarmCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s300AlarmAudibleAlarmCutoff.setStatus("current")
_S300Power_ObjectIdentity = ObjectIdentity
s300Power = _S300Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 5)
)
if mibBuilder.loadTexts:
    s300Power.setStatus("current")


class _S300PowerStatus_Type(Bits):
    """Custom type s300PowerStatus based on Bits"""
    namedValues = NamedValues(
        *(("powerAFailed", 0),
          ("powerBFailed", 1),
          ("fuseFailed", 2))
    )

_S300PowerStatus_Type.__name__ = "Bits"
_S300PowerStatus_Object = MibScalar
s300PowerStatus = _S300PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 5, 1),
    _S300PowerStatus_Type()
)
s300PowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300PowerStatus.setStatus("current")
_S300SystemTraps_ObjectIdentity = ObjectIdentity
s300SystemTraps = _S300SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6)
)
if mibBuilder.loadTexts:
    s300SystemTraps.setStatus("current")
_S300SystemV2Traps_ObjectIdentity = ObjectIdentity
s300SystemV2Traps = _S300SystemV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6, 0)
)
if mibBuilder.loadTexts:
    s300SystemV2Traps.setStatus("current")
_S300StaticRoute_ObjectIdentity = ObjectIdentity
s300StaticRoute = _S300StaticRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7)
)
if mibBuilder.loadTexts:
    s300StaticRoute.setStatus("current")
_S300StaticRouteTable_Object = MibTable
s300StaticRouteTable = _S300StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    s300StaticRouteTable.setStatus("current")
_S300StaticRouteEntry_Object = MibTableRow
s300StaticRouteEntry = _S300StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1, 1)
)
s300StaticRouteEntry.setIndexNames(
    (0, "ZHONE-SECHTOR300-MIB", "s300StaticRouteDest"),
    (0, "ZHONE-SECHTOR300-MIB", "s300StaticRouteNetMask"),
    (0, "ZHONE-SECHTOR300-MIB", "s300StaticRouteNextHop"),
    (0, "ZHONE-SECHTOR300-MIB", "s300StaticRouteIfNumber"),
    (0, "ZHONE-SECHTOR300-MIB", "s300StaticRouteTpId"),
)
if mibBuilder.loadTexts:
    s300StaticRouteEntry.setStatus("current")
_S300StaticRouteDest_Type = IpAddress
_S300StaticRouteDest_Object = MibTableColumn
s300StaticRouteDest = _S300StaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1, 1, 1),
    _S300StaticRouteDest_Type()
)
s300StaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300StaticRouteDest.setStatus("current")
_S300StaticRouteNetMask_Type = IpAddress
_S300StaticRouteNetMask_Object = MibTableColumn
s300StaticRouteNetMask = _S300StaticRouteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1, 1, 2),
    _S300StaticRouteNetMask_Type()
)
s300StaticRouteNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300StaticRouteNetMask.setStatus("current")
_S300StaticRouteNextHop_Type = IpAddress
_S300StaticRouteNextHop_Object = MibTableColumn
s300StaticRouteNextHop = _S300StaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1, 1, 3),
    _S300StaticRouteNextHop_Type()
)
s300StaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300StaticRouteNextHop.setStatus("current")


class _S300StaticRouteIfNumber_Type(Integer32):
    """Custom type s300StaticRouteIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300StaticRouteIfNumber_Type.__name__ = "Integer32"
_S300StaticRouteIfNumber_Object = MibTableColumn
s300StaticRouteIfNumber = _S300StaticRouteIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1, 1, 4),
    _S300StaticRouteIfNumber_Type()
)
s300StaticRouteIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300StaticRouteIfNumber.setStatus("current")


class _S300StaticRouteTpId_Type(Integer32):
    """Custom type s300StaticRouteTpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_S300StaticRouteTpId_Type.__name__ = "Integer32"
_S300StaticRouteTpId_Object = MibTableColumn
s300StaticRouteTpId = _S300StaticRouteTpId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1, 1, 5),
    _S300StaticRouteTpId_Type()
)
s300StaticRouteTpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300StaticRouteTpId.setStatus("current")
_S300StaticRouteRowStatus_Type = ZhoneRowStatus
_S300StaticRouteRowStatus_Object = MibTableColumn
s300StaticRouteRowStatus = _S300StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 7, 1, 1, 6),
    _S300StaticRouteRowStatus_Type()
)
s300StaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300StaticRouteRowStatus.setStatus("current")
_S300NetworkTimeProtocol_ObjectIdentity = ObjectIdentity
s300NetworkTimeProtocol = _S300NetworkTimeProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8)
)
if mibBuilder.loadTexts:
    s300NetworkTimeProtocol.setStatus("current")
_S300NtpServerTable_Object = MibTable
s300NtpServerTable = _S300NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    s300NtpServerTable.setStatus("current")
_S300NtpServerEntry_Object = MibTableRow
s300NtpServerEntry = _S300NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1, 1)
)
s300NtpServerEntry.setIndexNames(
    (0, "ZHONE-SECHTOR300-MIB", "s300NtpServerIpAddress"),
)
if mibBuilder.loadTexts:
    s300NtpServerEntry.setStatus("current")
_S300NtpServerIpAddress_Type = IpAddress
_S300NtpServerIpAddress_Object = MibTableColumn
s300NtpServerIpAddress = _S300NtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1, 1, 1),
    _S300NtpServerIpAddress_Type()
)
s300NtpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    s300NtpServerIpAddress.setStatus("current")


class _S300NtpServerRole_Type(Integer32):
    """Custom type s300NtpServerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_S300NtpServerRole_Type.__name__ = "Integer32"
_S300NtpServerRole_Object = MibTableColumn
s300NtpServerRole = _S300NtpServerRole_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1, 1, 2),
    _S300NtpServerRole_Type()
)
s300NtpServerRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300NtpServerRole.setStatus("current")


class _S300NtpServerSyncStatus_Type(Integer32):
    """Custom type s300NtpServerSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSync", 1),
          ("outSync", 2))
    )


_S300NtpServerSyncStatus_Type.__name__ = "Integer32"
_S300NtpServerSyncStatus_Object = MibTableColumn
s300NtpServerSyncStatus = _S300NtpServerSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1, 1, 3),
    _S300NtpServerSyncStatus_Type()
)
s300NtpServerSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300NtpServerSyncStatus.setStatus("current")


class _S300NtpTimeStampOffset_Type(Integer32):
    """Custom type s300NtpTimeStampOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-43200, 43200),
    )


_S300NtpTimeStampOffset_Type.__name__ = "Integer32"
_S300NtpTimeStampOffset_Object = MibTableColumn
s300NtpTimeStampOffset = _S300NtpTimeStampOffset_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1, 1, 4),
    _S300NtpTimeStampOffset_Type()
)
s300NtpTimeStampOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300NtpTimeStampOffset.setStatus("current")
_S300NtpSyncRequestFrequency_Type = Unsigned32
_S300NtpSyncRequestFrequency_Object = MibTableColumn
s300NtpSyncRequestFrequency = _S300NtpSyncRequestFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1, 1, 5),
    _S300NtpSyncRequestFrequency_Type()
)
s300NtpSyncRequestFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300NtpSyncRequestFrequency.setStatus("current")
_S300NtpServerRowStatus_Type = ZhoneRowStatus
_S300NtpServerRowStatus_Object = MibTableColumn
s300NtpServerRowStatus = _S300NtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 8, 1, 1, 6),
    _S300NtpServerRowStatus_Type()
)
s300NtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    s300NtpServerRowStatus.setStatus("current")
_S300Fan_ObjectIdentity = ObjectIdentity
s300Fan = _S300Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 9)
)
if mibBuilder.loadTexts:
    s300Fan.setStatus("current")


class _S300FanStatus_Type(Integer32):
    """Custom type s300FanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("fault", 2))
    )


_S300FanStatus_Type.__name__ = "Integer32"
_S300FanStatus_Object = MibScalar
s300FanStatus = _S300FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 9, 1),
    _S300FanStatus_Type()
)
s300FanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s300FanStatus.setStatus("current")
_S300Groups_ObjectIdentity = ObjectIdentity
s300Groups = _S300Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    s300Groups.setStatus("current")
dsx1ConfigEntry.registerAugmentions(
    ("ZHONE-SECHTOR300-MIB",
     "s300BertEntry")
)
s300BertEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1ConfigEntry.registerAugmentions(
    ("ZHONE-SECHTOR300-MIB",
     "s300Ds1Entry")
)
s300Ds1Entry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx3ConfigEntry.registerAugmentions(
    ("ZHONE-SECHTOR300-MIB",
     "s300Ds3Entry")
)
s300Ds3Entry.setIndexNames(*dsx3ConfigEntry.getIndexNames())

# Managed Objects groups

s300EquipmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 4, 1)
)
s300EquipmentGroup.setObjects(
      *(("ZHONE-SECHTOR300-MIB", "s300IOCardIdentification"),
        ("ZHONE-SECHTOR300-MIB", "s300IOCardZhoneType"),
        ("ZHONE-SECHTOR300-MIB", "s300IOCardMfgSerialNumber"),
        ("ZHONE-SECHTOR300-MIB", "s300IOCardMfgDate"),
        ("ZHONE-SECHTOR300-MIB", "s300IOCardProductNumber"),
        ("ZHONE-SECHTOR300-MIB", "s300IOCardRevisionCode"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentType"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentMode"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentRedundancyMode"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentPriority"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentWorkingMode"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentAdminStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentOperStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentIOOperStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentFaultMap"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentRowStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentProtectionSlot"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentActiveSlot"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentSwitchAction"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentSwitchStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentProtectionStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300SoftwareLoadName"),
        ("ZHONE-SECHTOR300-MIB", "s300SoftwareBootName"),
        ("ZHONE-SECHTOR300-MIB", "s300SoftwareFpga1Name"),
        ("ZHONE-SECHTOR300-MIB", "s300SoftwareFpga2Name"),
        ("ZHONE-SECHTOR300-MIB", "s300SoftwareCpldName"),
        ("ZHONE-SECHTOR300-MIB", "s300SoftwareBspName"),
        ("ZHONE-SECHTOR300-MIB", "s300SoftwareBankStatus"))
)
if mibBuilder.loadTexts:
    s300EquipmentGroup.setStatus("current")

s300DsxGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 4, 2)
)
s300DsxGroup.setObjects(
      *(("ZHONE-SECHTOR300-MIB", "s300NextTpId"),
        ("ZHONE-SECHTOR300-MIB", "s300NextCrsId"),
        ("ZHONE-SECHTOR300-MIB", "s300TsMap"),
        ("ZHONE-SECHTOR300-MIB", "s300TpIfIndex"),
        ("ZHONE-SECHTOR300-MIB", "s300TpTrafficType"),
        ("ZHONE-SECHTOR300-MIB", "s300TpType"),
        ("ZHONE-SECHTOR300-MIB", "s300TpTcABCD1"),
        ("ZHONE-SECHTOR300-MIB", "s300TpTcABCD2"),
        ("ZHONE-SECHTOR300-MIB", "s300TpSigCnv"),
        ("ZHONE-SECHTOR300-MIB", "s300TpSigConversionRxId"),
        ("ZHONE-SECHTOR300-MIB", "s300TpSigConversionTxId"),
        ("ZHONE-SECHTOR300-MIB", "s300TpDiag"),
        ("ZHONE-SECHTOR300-MIB", "s300TpCrsId"),
        ("ZHONE-SECHTOR300-MIB", "s300TpRowStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300CrsPrimaryTpId"),
        ("ZHONE-SECHTOR300-MIB", "s300CrsBidirectionalTpId"),
        ("ZHONE-SECHTOR300-MIB", "s300CrsName"),
        ("ZHONE-SECHTOR300-MIB", "s300CrsType"),
        ("ZHONE-SECHTOR300-MIB", "s300CrsRowStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300CrsUniLeafRowStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300BertType"),
        ("ZHONE-SECHTOR300-MIB", "s300BertAdmin"),
        ("ZHONE-SECHTOR300-MIB", "s300BertInsertBitError"),
        ("ZHONE-SECHTOR300-MIB", "s300BertElaspedTime"),
        ("ZHONE-SECHTOR300-MIB", "s300BertSeverelyErroredSeconds"),
        ("ZHONE-SECHTOR300-MIB", "s300BertOutOfSynchSeconds"),
        ("ZHONE-SECHTOR300-MIB", "s300BertBitErrorRate"),
        ("ZHONE-SECHTOR300-MIB", "s300BertClearStats"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1OtherFdlType"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1FarEndLoopbackConfig"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1FarEndLoopbackCtrl"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1Conversion"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1SigConversionRxId"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1SigConversionTxId"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1LineBuildOut"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds1ConnectorType"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0000"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0001"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0010"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0011"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0100"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0101"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0110"),
        ("ZHONE-SECHTOR300-MIB", "sigRx0111"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1000"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1001"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1010"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1011"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1100"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1101"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1110"),
        ("ZHONE-SECHTOR300-MIB", "sigRx1111"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0000"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0001"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0010"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0011"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0100"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0101"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0110"),
        ("ZHONE-SECHTOR300-MIB", "sigTx0111"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1000"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1001"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1010"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1011"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1100"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1101"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1110"),
        ("ZHONE-SECHTOR300-MIB", "sigTx1111"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds3LineStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds3AisTxFormat"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds3AisDetFormat"),
        ("ZHONE-SECHTOR300-MIB", "s300Ds3LoopbackConfig"))
)
if mibBuilder.loadTexts:
    s300DsxGroup.setStatus("current")

s300SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 4, 3)
)
s300SystemGroup.setObjects(
      *(("ZHONE-SECHTOR300-MIB", "s300FileTransferSlot"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferBankNumber"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferServerAddress"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferRemoteFileName"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferFileType"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferType"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferAdmin"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300FileTransferFault"),
        ("ZHONE-SECHTOR300-MIB", "s300NvmInit"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc1Type"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc1Ifindex"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc2Type"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc2Ifindex"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc3Type"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc3Ifindex"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc4Type"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrc4Ifindex"),
        ("ZHONE-SECHTOR300-MIB", "s300TimingClksrcActiveClock"),
        ("ZHONE-SECHTOR300-MIB", "s300AlarmAudibleAlarmCutoff"),
        ("ZHONE-SECHTOR300-MIB", "s300PowerStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300StaticRouteRowStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300NtpServerRole"),
        ("ZHONE-SECHTOR300-MIB", "s300NtpServerSyncStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300NtpTimeStampOffset"),
        ("ZHONE-SECHTOR300-MIB", "s300NtpSyncRequestFrequency"),
        ("ZHONE-SECHTOR300-MIB", "s300NtpServerRowStatus"),
        ("ZHONE-SECHTOR300-MIB", "s300FanStatus"))
)
if mibBuilder.loadTexts:
    s300SystemGroup.setStatus("current")


# Notification objects

s300EquipmentOperStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 5, 0, 1)
)
s300EquipmentOperStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300EquipmentOperStatus")
)
if mibBuilder.loadTexts:
    s300EquipmentOperStatusChangeTrap.setStatus(
        "current"
    )

s300EquipmentGroupProtectionStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 5, 0, 2)
)
s300EquipmentGroupProtectionStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300EquipmentProtectionStatus")
)
if mibBuilder.loadTexts:
    s300EquipmentGroupProtectionStatusChangeTrap.setStatus(
        "current"
    )

s300EquipmentGroupSwitchStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 5, 0, 3)
)
s300EquipmentGroupSwitchStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300EquipmentSwitchStatus")
)
if mibBuilder.loadTexts:
    s300EquipmentGroupSwitchStatusChangeTrap.setStatus(
        "current"
    )

s300EquipmentIOOperStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 5, 0, 4)
)
s300EquipmentIOOperStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300EquipmentIOOperStatus")
)
if mibBuilder.loadTexts:
    s300EquipmentIOOperStatusChangeTrap.setStatus(
        "current"
    )

s300EquipmentFaultMapChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 1, 5, 0, 5)
)
s300EquipmentFaultMapChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300EquipmentFaultMap")
)
if mibBuilder.loadTexts:
    s300EquipmentFaultMapChangeTrap.setStatus(
        "current"
    )

s300Ds3LineStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 2, 5, 2, 0, 1)
)
s300Ds3LineStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300Ds3LineStatus")
)
if mibBuilder.loadTexts:
    s300Ds3LineStatusChangeTrap.setStatus(
        "current"
    )

s300SystemFileTransferStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6, 0, 1)
)
s300SystemFileTransferStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300FileTransferStatus")
)
if mibBuilder.loadTexts:
    s300SystemFileTransferStatusChangeTrap.setStatus(
        "current"
    )

s300SystemActiveClockChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6, 0, 2)
)
s300SystemActiveClockChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300TimingClksrcActiveClock")
)
if mibBuilder.loadTexts:
    s300SystemActiveClockChangeTrap.setStatus(
        "current"
    )

s300SystemPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6, 0, 3)
)
s300SystemPowerStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300PowerStatus")
)
if mibBuilder.loadTexts:
    s300SystemPowerStatusChangeTrap.setStatus(
        "current"
    )

s300SystemAlarmAudibleAlarmCutoffChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6, 0, 4)
)
s300SystemAlarmAudibleAlarmCutoffChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300AlarmAudibleAlarmCutoff")
)
if mibBuilder.loadTexts:
    s300SystemAlarmAudibleAlarmCutoffChangeTrap.setStatus(
        "current"
    )

s300NtpServerSyncStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6, 0, 5)
)
s300NtpServerSyncStatusChange.setObjects(
      *(("ZHONE-SECHTOR300-MIB", "s300NtpServerRole"),
        ("ZHONE-SECHTOR300-MIB", "s300NtpServerSyncStatus"))
)
if mibBuilder.loadTexts:
    s300NtpServerSyncStatusChange.setStatus(
        "current"
    )

s300SystemFanStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 3, 6, 0, 6)
)
s300SystemFanStatusChangeTrap.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300FanStatus")
)
if mibBuilder.loadTexts:
    s300SystemFanStatusChangeTrap.setStatus(
        "current"
    )


# Notifications groups

s300EquipmentTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 4, 4)
)
s300EquipmentTrapsGroup.setObjects(
      *(("ZHONE-SECHTOR300-MIB", "s300EquipmentOperStatusChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentGroupProtectionStatusChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentGroupSwitchStatusChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentIOOperStatusChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300EquipmentFaultMapChangeTrap"))
)
if mibBuilder.loadTexts:
    s300EquipmentTrapsGroup.setStatus(
        "current"
    )

s300SystemTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 4, 5)
)
s300SystemTrapsGroup.setObjects(
      *(("ZHONE-SECHTOR300-MIB", "s300SystemFileTransferStatusChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300SystemActiveClockChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300SystemPowerStatusChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300SystemAlarmAudibleAlarmCutoffChangeTrap"),
        ("ZHONE-SECHTOR300-MIB", "s300NtpServerSyncStatusChange"),
        ("ZHONE-SECHTOR300-MIB", "s300SystemFanStatusChangeTrap"))
)
if mibBuilder.loadTexts:
    s300SystemTrapsGroup.setStatus(
        "current"
    )

s300DsxTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 4, 2, 4, 6)
)
s300DsxTrapsGroup.setObjects(
    ("ZHONE-SECHTOR300-MIB", "s300Ds3LineStatusChangeTrap")
)
if mibBuilder.loadTexts:
    s300DsxTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-SECHTOR300-MIB",
    **{"ZhoneABCDValue": ZhoneABCDValue,
       "s300Equipment": s300Equipment,
       "s300IOCardResourceTable": s300IOCardResourceTable,
       "s300IOCardResourceEntry": s300IOCardResourceEntry,
       "s300IOCardIdentification": s300IOCardIdentification,
       "s300IOCardZhoneType": s300IOCardZhoneType,
       "s300IOCardMfgSerialNumber": s300IOCardMfgSerialNumber,
       "s300IOCardMfgDate": s300IOCardMfgDate,
       "s300IOCardProductNumber": s300IOCardProductNumber,
       "s300IOCardRevisionCode": s300IOCardRevisionCode,
       "s300EquipmentConfigTable": s300EquipmentConfigTable,
       "s300EquipmentConfigEntry": s300EquipmentConfigEntry,
       "s300EquipmentType": s300EquipmentType,
       "s300EquipmentMode": s300EquipmentMode,
       "s300EquipmentRedundancyMode": s300EquipmentRedundancyMode,
       "s300EquipmentPriority": s300EquipmentPriority,
       "s300EquipmentWorkingMode": s300EquipmentWorkingMode,
       "s300EquipmentAdminStatus": s300EquipmentAdminStatus,
       "s300EquipmentOperStatus": s300EquipmentOperStatus,
       "s300EquipmentIOOperStatus": s300EquipmentIOOperStatus,
       "s300EquipmentFaultMap": s300EquipmentFaultMap,
       "s300EquipmentRowStatus": s300EquipmentRowStatus,
       "s300EquipmentProtectionTable": s300EquipmentProtectionTable,
       "s300EquipmentProtectionEntry": s300EquipmentProtectionEntry,
       "s300EquipmentProtectionSlot": s300EquipmentProtectionSlot,
       "s300EquipmentActiveSlot": s300EquipmentActiveSlot,
       "s300EquipmentSwitchAction": s300EquipmentSwitchAction,
       "s300EquipmentSwitchStatus": s300EquipmentSwitchStatus,
       "s300EquipmentProtectionStatus": s300EquipmentProtectionStatus,
       "s300SoftwareTable": s300SoftwareTable,
       "s300SoftwareEntry": s300SoftwareEntry,
       "s300SoftwareBankNumber": s300SoftwareBankNumber,
       "s300SoftwareLoadName": s300SoftwareLoadName,
       "s300SoftwareBootName": s300SoftwareBootName,
       "s300SoftwareFpga1Name": s300SoftwareFpga1Name,
       "s300SoftwareFpga2Name": s300SoftwareFpga2Name,
       "s300SoftwareCpldName": s300SoftwareCpldName,
       "s300SoftwareBspName": s300SoftwareBspName,
       "s300SoftwareBankStatus": s300SoftwareBankStatus,
       "s300EquipmentTraps": s300EquipmentTraps,
       "s300EquipmentV2Traps": s300EquipmentV2Traps,
       "s300EquipmentOperStatusChangeTrap": s300EquipmentOperStatusChangeTrap,
       "s300EquipmentGroupProtectionStatusChangeTrap": s300EquipmentGroupProtectionStatusChangeTrap,
       "s300EquipmentGroupSwitchStatusChangeTrap": s300EquipmentGroupSwitchStatusChangeTrap,
       "s300EquipmentIOOperStatusChangeTrap": s300EquipmentIOOperStatusChangeTrap,
       "s300EquipmentFaultMapChangeTrap": s300EquipmentFaultMapChangeTrap,
       "s300Dsx": s300Dsx,
       "s300TdmXcon": s300TdmXcon,
       "s300NextTpId": s300NextTpId,
       "s300NextCrsId": s300NextCrsId,
       "s300TpTable": s300TpTable,
       "s300TpEntry": s300TpEntry,
       "s300TpId": s300TpId,
       "s300TsMap": s300TsMap,
       "s300TpIfIndex": s300TpIfIndex,
       "s300TpTrafficType": s300TpTrafficType,
       "s300TpType": s300TpType,
       "s300TpTcABCD1": s300TpTcABCD1,
       "s300TpTcABCD2": s300TpTcABCD2,
       "s300TpSigCnv": s300TpSigCnv,
       "s300TpSigConversionRxId": s300TpSigConversionRxId,
       "s300TpSigConversionTxId": s300TpSigConversionTxId,
       "s300TpDiag": s300TpDiag,
       "s300TpCrsId": s300TpCrsId,
       "s300TpRowStatus": s300TpRowStatus,
       "s300CrsTable": s300CrsTable,
       "s300CrsEntry": s300CrsEntry,
       "s300CrsId": s300CrsId,
       "s300CrsPrimaryTpId": s300CrsPrimaryTpId,
       "s300CrsBidirectionalTpId": s300CrsBidirectionalTpId,
       "s300CrsName": s300CrsName,
       "s300CrsType": s300CrsType,
       "s300CrsRowStatus": s300CrsRowStatus,
       "s300CrsBroadcastTable": s300CrsBroadcastTable,
       "s300CrsBroadcastEntry": s300CrsBroadcastEntry,
       "s300CrsUniLeafRowStatus": s300CrsUniLeafRowStatus,
       "s300Bert": s300Bert,
       "s300BertTable": s300BertTable,
       "s300BertEntry": s300BertEntry,
       "s300BertType": s300BertType,
       "s300BertAdmin": s300BertAdmin,
       "s300BertInsertBitError": s300BertInsertBitError,
       "s300BertElaspedTime": s300BertElaspedTime,
       "s300BertSeverelyErroredSeconds": s300BertSeverelyErroredSeconds,
       "s300BertOutOfSynchSeconds": s300BertOutOfSynchSeconds,
       "s300BertBitErrorRate": s300BertBitErrorRate,
       "s300BertClearStats": s300BertClearStats,
       "s300Ds1": s300Ds1,
       "s300Ds1Table": s300Ds1Table,
       "s300Ds1Entry": s300Ds1Entry,
       "s300Ds1OtherFdlType": s300Ds1OtherFdlType,
       "s300Ds1FarEndLoopbackConfig": s300Ds1FarEndLoopbackConfig,
       "s300Ds1FarEndLoopbackCtrl": s300Ds1FarEndLoopbackCtrl,
       "s300Ds1Conversion": s300Ds1Conversion,
       "s300Ds1SigConversionRxId": s300Ds1SigConversionRxId,
       "s300Ds1SigConversionTxId": s300Ds1SigConversionTxId,
       "s300Ds1LineBuildOut": s300Ds1LineBuildOut,
       "s300Ds1ConnectorType": s300Ds1ConnectorType,
       "s300SigConversion": s300SigConversion,
       "s300SigConversionRxTable": s300SigConversionRxTable,
       "s300SigConversionRxEntry": s300SigConversionRxEntry,
       "sigConversionRxIdentification": sigConversionRxIdentification,
       "sigRx0000": sigRx0000,
       "sigRx0001": sigRx0001,
       "sigRx0010": sigRx0010,
       "sigRx0011": sigRx0011,
       "sigRx0100": sigRx0100,
       "sigRx0101": sigRx0101,
       "sigRx0110": sigRx0110,
       "sigRx0111": sigRx0111,
       "sigRx1000": sigRx1000,
       "sigRx1001": sigRx1001,
       "sigRx1010": sigRx1010,
       "sigRx1011": sigRx1011,
       "sigRx1100": sigRx1100,
       "sigRx1101": sigRx1101,
       "sigRx1110": sigRx1110,
       "sigRx1111": sigRx1111,
       "s300SigConversionTxTable": s300SigConversionTxTable,
       "s300SigConversionTxEntry": s300SigConversionTxEntry,
       "sigConversionTxIdentification": sigConversionTxIdentification,
       "sigTx0000": sigTx0000,
       "sigTx0001": sigTx0001,
       "sigTx0010": sigTx0010,
       "sigTx0011": sigTx0011,
       "sigTx0100": sigTx0100,
       "sigTx0101": sigTx0101,
       "sigTx0110": sigTx0110,
       "sigTx0111": sigTx0111,
       "sigTx1000": sigTx1000,
       "sigTx1001": sigTx1001,
       "sigTx1010": sigTx1010,
       "sigTx1011": sigTx1011,
       "sigTx1100": sigTx1100,
       "sigTx1101": sigTx1101,
       "sigTx1110": sigTx1110,
       "sigTx1111": sigTx1111,
       "s300Ds3": s300Ds3,
       "s300Ds3Table": s300Ds3Table,
       "s300Ds3Entry": s300Ds3Entry,
       "s300Ds3LineStatus": s300Ds3LineStatus,
       "s300Ds3AisTxFormat": s300Ds3AisTxFormat,
       "s300Ds3AisDetFormat": s300Ds3AisDetFormat,
       "s300Ds3LoopbackConfig": s300Ds3LoopbackConfig,
       "s300Ds3Traps": s300Ds3Traps,
       "s300Ds3V2Traps": s300Ds3V2Traps,
       "s300Ds3LineStatusChangeTrap": s300Ds3LineStatusChangeTrap,
       "s300System": s300System,
       "s300FileTransfer": s300FileTransfer,
       "s300FileTransferSlot": s300FileTransferSlot,
       "s300FileTransferBankNumber": s300FileTransferBankNumber,
       "s300FileTransferServerAddress": s300FileTransferServerAddress,
       "s300FileTransferRemoteFileName": s300FileTransferRemoteFileName,
       "s300FileTransferFileType": s300FileTransferFileType,
       "s300FileTransferType": s300FileTransferType,
       "s300FileTransferAdmin": s300FileTransferAdmin,
       "s300FileTransferStatus": s300FileTransferStatus,
       "s300FileTransferFault": s300FileTransferFault,
       "s300Nvm": s300Nvm,
       "s300NvmInit": s300NvmInit,
       "s300Timing": s300Timing,
       "s300TimingConfig": s300TimingConfig,
       "s300TimingClksrc1Type": s300TimingClksrc1Type,
       "s300TimingClksrc1Ifindex": s300TimingClksrc1Ifindex,
       "s300TimingClksrc2Type": s300TimingClksrc2Type,
       "s300TimingClksrc2Ifindex": s300TimingClksrc2Ifindex,
       "s300TimingClksrc3Type": s300TimingClksrc3Type,
       "s300TimingClksrc3Ifindex": s300TimingClksrc3Ifindex,
       "s300TimingClksrc4Type": s300TimingClksrc4Type,
       "s300TimingClksrc4Ifindex": s300TimingClksrc4Ifindex,
       "s300TimingClksrcActiveClock": s300TimingClksrcActiveClock,
       "s300Alarms": s300Alarms,
       "s300AlarmAudibleAlarmCutoff": s300AlarmAudibleAlarmCutoff,
       "s300Power": s300Power,
       "s300PowerStatus": s300PowerStatus,
       "s300SystemTraps": s300SystemTraps,
       "s300SystemV2Traps": s300SystemV2Traps,
       "s300SystemFileTransferStatusChangeTrap": s300SystemFileTransferStatusChangeTrap,
       "s300SystemActiveClockChangeTrap": s300SystemActiveClockChangeTrap,
       "s300SystemPowerStatusChangeTrap": s300SystemPowerStatusChangeTrap,
       "s300SystemAlarmAudibleAlarmCutoffChangeTrap": s300SystemAlarmAudibleAlarmCutoffChangeTrap,
       "s300NtpServerSyncStatusChange": s300NtpServerSyncStatusChange,
       "s300SystemFanStatusChangeTrap": s300SystemFanStatusChangeTrap,
       "s300StaticRoute": s300StaticRoute,
       "s300StaticRouteTable": s300StaticRouteTable,
       "s300StaticRouteEntry": s300StaticRouteEntry,
       "s300StaticRouteDest": s300StaticRouteDest,
       "s300StaticRouteNetMask": s300StaticRouteNetMask,
       "s300StaticRouteNextHop": s300StaticRouteNextHop,
       "s300StaticRouteIfNumber": s300StaticRouteIfNumber,
       "s300StaticRouteTpId": s300StaticRouteTpId,
       "s300StaticRouteRowStatus": s300StaticRouteRowStatus,
       "s300NetworkTimeProtocol": s300NetworkTimeProtocol,
       "s300NtpServerTable": s300NtpServerTable,
       "s300NtpServerEntry": s300NtpServerEntry,
       "s300NtpServerIpAddress": s300NtpServerIpAddress,
       "s300NtpServerRole": s300NtpServerRole,
       "s300NtpServerSyncStatus": s300NtpServerSyncStatus,
       "s300NtpTimeStampOffset": s300NtpTimeStampOffset,
       "s300NtpSyncRequestFrequency": s300NtpSyncRequestFrequency,
       "s300NtpServerRowStatus": s300NtpServerRowStatus,
       "s300Fan": s300Fan,
       "s300FanStatus": s300FanStatus,
       "s300Groups": s300Groups,
       "s300EquipmentGroup": s300EquipmentGroup,
       "s300DsxGroup": s300DsxGroup,
       "s300SystemGroup": s300SystemGroup,
       "s300EquipmentTrapsGroup": s300EquipmentTrapsGroup,
       "s300SystemTrapsGroup": s300SystemTrapsGroup,
       "s300DsxTrapsGroup": s300DsxTrapsGroup,
       "zhoneSechtor300": zhoneSechtor300}
)

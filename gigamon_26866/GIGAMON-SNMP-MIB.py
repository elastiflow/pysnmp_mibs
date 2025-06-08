# SNMP MIB module (GIGAMON-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/gigamon_26866/GIGAMON-SNMP-MIB-GV7100.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:14:46 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

gigamonSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26866)
)
if mibBuilder.loadTexts:
    gigamonSnmp.setRevisions(
        ("2010-07-10 10:00",
         "2010-07-10 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GigamonSnmpNotifications_ObjectIdentity = ObjectIdentity
gigamonSnmpNotifications = _GigamonSnmpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1)
)
_GigamonGigaVUE_ObjectIdentity = ObjectIdentity
gigamonGigaVUE = _GigamonGigaVUE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1)
)
_GigamonSnmpNotificationObjects_ObjectIdentity = ObjectIdentity
gigamonSnmpNotificationObjects = _GigamonSnmpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2)
)


class _GigamonSnmpNotifLevel_Type(Integer32):
    """Custom type gigamonSnmpNotifLevel based on Integer32"""
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
        *(("information", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_GigamonSnmpNotifLevel_Type.__name__ = "Integer32"
_GigamonSnmpNotifLevel_Object = MibScalar
gigamonSnmpNotifLevel = _GigamonSnmpNotifLevel_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 1),
    _GigamonSnmpNotifLevel_Type()
)
gigamonSnmpNotifLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifLevel.setStatus("current")
_GigamonSnmpNotifDescription_Type = OctetString
_GigamonSnmpNotifDescription_Object = MibScalar
gigamonSnmpNotifDescription = _GigamonSnmpNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 2),
    _GigamonSnmpNotifDescription_Type()
)
gigamonSnmpNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifDescription.setStatus("current")


class _GigamonSnmpNotifOpType_Type(Integer32):
    """Custom type gigamonSnmpNotifOpType based on Integer32"""
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
        *(("read", 1),
          ("write", 2),
          ("delete", 3),
          ("validate", 4),
          ("change", 5))
    )


_GigamonSnmpNotifOpType_Type.__name__ = "Integer32"
_GigamonSnmpNotifOpType_Object = MibScalar
gigamonSnmpNotifOpType = _GigamonSnmpNotifOpType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 3),
    _GigamonSnmpNotifOpType_Type()
)
gigamonSnmpNotifOpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifOpType.setStatus("current")
_GigamonSnmpNotifPortName_Type = OctetString
_GigamonSnmpNotifPortName_Object = MibScalar
gigamonSnmpNotifPortName = _GigamonSnmpNotifPortName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 4),
    _GigamonSnmpNotifPortName_Type()
)
gigamonSnmpNotifPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifPortName.setStatus("current")


class _GigamonSnmpNotifPortLinkStatus_Type(Integer32):
    """Custom type gigamonSnmpNotifPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_GigamonSnmpNotifPortLinkStatus_Type.__name__ = "Integer32"
_GigamonSnmpNotifPortLinkStatus_Object = MibScalar
gigamonSnmpNotifPortLinkStatus = _GigamonSnmpNotifPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 5),
    _GigamonSnmpNotifPortLinkStatus_Type()
)
gigamonSnmpNotifPortLinkStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifPortLinkStatus.setStatus("current")


class _GigamonSnmpNotifTAPRelayStatus_Type(Integer32):
    """Custom type gigamonSnmpNotifTAPRelayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("passive", 1),
          ("active", 2))
    )


_GigamonSnmpNotifTAPRelayStatus_Type.__name__ = "Integer32"
_GigamonSnmpNotifTAPRelayStatus_Object = MibScalar
gigamonSnmpNotifTAPRelayStatus = _GigamonSnmpNotifTAPRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 6),
    _GigamonSnmpNotifTAPRelayStatus_Type()
)
gigamonSnmpNotifTAPRelayStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifTAPRelayStatus.setStatus("current")


class _GigamonSnmpNotifRxTxType_Type(Integer32):
    """Custom type gigamonSnmpNotifRxTxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rx", 0),
          ("tx", 1))
    )


_GigamonSnmpNotifRxTxType_Type.__name__ = "Integer32"
_GigamonSnmpNotifRxTxType_Object = MibScalar
gigamonSnmpNotifRxTxType = _GigamonSnmpNotifRxTxType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 7),
    _GigamonSnmpNotifRxTxType_Type()
)
gigamonSnmpNotifRxTxType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifRxTxType.setStatus("current")


class _GigamonSnmpNotifRxTxErrorType_Type(Integer32):
    """Custom type gigamonSnmpNotifRxTxErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("under-size", 0),
          ("fragments", 1),
          ("obsolete", 2),
          ("jabbers", 3),
          ("crc-align", 4),
          ("unknown", 5))
    )


_GigamonSnmpNotifRxTxErrorType_Type.__name__ = "Integer32"
_GigamonSnmpNotifRxTxErrorType_Object = MibScalar
gigamonSnmpNotifRxTxErrorType = _GigamonSnmpNotifRxTxErrorType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 8),
    _GigamonSnmpNotifRxTxErrorType_Type()
)
gigamonSnmpNotifRxTxErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifRxTxErrorType.setStatus("current")
_GigamonSnmpNotifCounter_Type = Integer32
_GigamonSnmpNotifCounter_Object = MibScalar
gigamonSnmpNotifCounter = _GigamonSnmpNotifCounter_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 9),
    _GigamonSnmpNotifCounter_Type()
)
gigamonSnmpNotifCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifCounter.setStatus("current")
_GigamonSnmpNotifFirmwareName_Type = OctetString
_GigamonSnmpNotifFirmwareName_Object = MibScalar
gigamonSnmpNotifFirmwareName = _GigamonSnmpNotifFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 10),
    _GigamonSnmpNotifFirmwareName_Type()
)
gigamonSnmpNotifFirmwareName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifFirmwareName.setStatus("current")


class _GigamonSnmpNotifModuleOperationType_Type(Integer32):
    """Custom type gigamonSnmpNotifModuleOperationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("removed", 0),
          ("inserted", 1),
          ("changed", 2))
    )


_GigamonSnmpNotifModuleOperationType_Type.__name__ = "Integer32"
_GigamonSnmpNotifModuleOperationType_Object = MibScalar
gigamonSnmpNotifModuleOperationType = _GigamonSnmpNotifModuleOperationType_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 11),
    _GigamonSnmpNotifModuleOperationType_Type()
)
gigamonSnmpNotifModuleOperationType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifModuleOperationType.setStatus("current")
_GigamonSnmpNotifModuleName_Type = OctetString
_GigamonSnmpNotifModuleName_Object = MibScalar
gigamonSnmpNotifModuleName = _GigamonSnmpNotifModuleName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 12),
    _GigamonSnmpNotifModuleName_Type()
)
gigamonSnmpNotifModuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifModuleName.setStatus("current")


class _GigamonNotifSlotNumber_Type(Integer32):
    """Custom type gigamonNotifSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mid-plane", 0),
          ("slot-1", 1),
          ("slot-2", 2),
          ("slot-3", 3),
          ("gigaLink-Back", 4),
          ("daughter-Card", 5))
    )


_GigamonNotifSlotNumber_Type.__name__ = "Integer32"
_GigamonNotifSlotNumber_Object = MibScalar
gigamonNotifSlotNumber = _GigamonNotifSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 13),
    _GigamonNotifSlotNumber_Type()
)
gigamonNotifSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonNotifSlotNumber.setStatus("current")
_GigamonSnmpNotifUserName_Type = OctetString
_GigamonSnmpNotifUserName_Object = MibScalar
gigamonSnmpNotifUserName = _GigamonSnmpNotifUserName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 14),
    _GigamonSnmpNotifUserName_Type()
)
gigamonSnmpNotifUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifUserName.setStatus("current")
_GigamonSnmpNotifFileName_Type = OctetString
_GigamonSnmpNotifFileName_Object = MibScalar
gigamonSnmpNotifFileName = _GigamonSnmpNotifFileName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 15),
    _GigamonSnmpNotifFileName_Type()
)
gigamonSnmpNotifFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifFileName.setStatus("current")


class _GigamonNotifPowerStatus_Type(Integer32):
    """Custom type gigamonNotifPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 0),
          ("normal", 1))
    )


_GigamonNotifPowerStatus_Type.__name__ = "Integer32"
_GigamonNotifPowerStatus_Object = MibScalar
gigamonNotifPowerStatus = _GigamonNotifPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 16),
    _GigamonNotifPowerStatus_Type()
)
gigamonNotifPowerStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonNotifPowerStatus.setStatus("current")
_GigamonSnmpNotifHardWareName_Type = OctetString
_GigamonSnmpNotifHardWareName_Object = MibScalar
gigamonSnmpNotifHardWareName = _GigamonSnmpNotifHardWareName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 17),
    _GigamonSnmpNotifHardWareName_Type()
)
gigamonSnmpNotifHardWareName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifHardWareName.setStatus("current")


class _GigamonSnmpNotifGigaVUE420SlotNumber_Type(Integer32):
    """Custom type gigamonSnmpNotifGigaVUE420SlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("mid-plane", 0),
          ("expansion-slot-1", 1),
          ("expansion-slot-2", 2),
          ("expansion-slot-3", 3),
          ("expansion-slot-4", 4),
          ("expansion-slot-5", 5),
          ("x1-slot", 6),
          ("x2-slot", 7),
          ("x3-slot", 8),
          ("x4-slot", 9))
    )


_GigamonSnmpNotifGigaVUE420SlotNumber_Type.__name__ = "Integer32"
_GigamonSnmpNotifGigaVUE420SlotNumber_Object = MibScalar
gigamonSnmpNotifGigaVUE420SlotNumber = _GigamonSnmpNotifGigaVUE420SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 18),
    _GigamonSnmpNotifGigaVUE420SlotNumber_Type()
)
gigamonSnmpNotifGigaVUE420SlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifGigaVUE420SlotNumber.setStatus("current")
_GigamonSnmpNotifFanName_Type = OctetString
_GigamonSnmpNotifFanName_Object = MibScalar
gigamonSnmpNotifFanName = _GigamonSnmpNotifFanName_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 19),
    _GigamonSnmpNotifFanName_Type()
)
gigamonSnmpNotifFanName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifFanName.setStatus("current")


class _GigamonNotifFanStatus_Type(Integer32):
    """Custom type gigamonNotifFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", -1),
          ("abnormal", 0),
          ("normal", 1))
    )


_GigamonNotifFanStatus_Type.__name__ = "Integer32"
_GigamonNotifFanStatus_Object = MibScalar
gigamonNotifFanStatus = _GigamonNotifFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 20),
    _GigamonNotifFanStatus_Type()
)
gigamonNotifFanStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonNotifFanStatus.setStatus("current")


class _GigamonSnmpNotifUtilizationAlarm_Type(Integer32):
    """Custom type gigamonSnmpNotifUtilizationAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("below", 0),
          ("exceed", 1))
    )


_GigamonSnmpNotifUtilizationAlarm_Type.__name__ = "Integer32"
_GigamonSnmpNotifUtilizationAlarm_Object = MibScalar
gigamonSnmpNotifUtilizationAlarm = _GigamonSnmpNotifUtilizationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 21),
    _GigamonSnmpNotifUtilizationAlarm_Type()
)
gigamonSnmpNotifUtilizationAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifUtilizationAlarm.setStatus("current")
_GigamonSnmpNotifUtilizationThreshold_Type = Integer32
_GigamonSnmpNotifUtilizationThreshold_Object = MibScalar
gigamonSnmpNotifUtilizationThreshold = _GigamonSnmpNotifUtilizationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 26866, 1, 2, 22),
    _GigamonSnmpNotifUtilizationThreshold_Type()
)
gigamonSnmpNotifUtilizationThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    gigamonSnmpNotifUtilizationThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

gigamonSnmpResetSystemNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 1)
)
gigamonSnmpResetSystemNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"))
)
if mibBuilder.loadTexts:
    gigamonSnmpResetSystemNotification.setStatus(
        "current"
    )

gigamonSnmpUserAuthFailNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 2)
)
gigamonSnmpUserAuthFailNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUserName"))
)
if mibBuilder.loadTexts:
    gigamonSnmpUserAuthFailNotification.setStatus(
        "current"
    )

gigamonSnmpFirmwareChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 3)
)
gigamonSnmpFirmwareChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFirmwareName"))
)
if mibBuilder.loadTexts:
    gigamonSnmpFirmwareChangeNotification.setStatus(
        "current"
    )

gigamonSnmpConfigSaveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 4)
)
gigamonSnmpConfigSaveNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFileName"))
)
if mibBuilder.loadTexts:
    gigamonSnmpConfigSaveNotification.setStatus(
        "current"
    )

gigamonSnmpModuleChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 5)
)
gigamonSnmpModuleChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleOperationType"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifModuleName"),
        ("GIGAMON-SNMP-MIB", "gigamonNotifSlotNumber"))
)
if mibBuilder.loadTexts:
    gigamonSnmpModuleChangeNotification.setStatus(
        "current"
    )

gigamonSnmpPacketDropNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 6)
)
gigamonSnmpPacketDropNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
)
if mibBuilder.loadTexts:
    gigamonSnmpPacketDropNotification.setStatus(
        "current"
    )

gigamonSnmpTapRelayChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 7)
)
gigamonSnmpTapRelayChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifTAPRelayStatus"))
)
if mibBuilder.loadTexts:
    gigamonSnmpTapRelayChangeNotification.setStatus(
        "current"
    )

gigamonSnmpPortLinkChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 8)
)
gigamonSnmpPortLinkChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortLinkStatus"))
)
if mibBuilder.loadTexts:
    gigamonSnmpPortLinkChangeNotification.setStatus(
        "current"
    )

gigamonSnmpRxTxErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 9)
)
gigamonSnmpRxTxErrorNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxType"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifRxTxErrorType"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifCounter"))
)
if mibBuilder.loadTexts:
    gigamonSnmpRxTxErrorNotification.setStatus(
        "current"
    )

gigamonPowerChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 10)
)
gigamonPowerChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonNotifPowerStatus"))
)
if mibBuilder.loadTexts:
    gigamonPowerChangeNotification.setStatus(
        "current"
    )

gigamonFanChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 11)
)
gigamonFanChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifFanName"),
        ("GIGAMON-SNMP-MIB", "gigamonNotifFanStatus"))
)
if mibBuilder.loadTexts:
    gigamonFanChangeNotification.setStatus(
        "current"
    )

gigamonSnmpOverThresholdChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 26866, 1, 1, 12)
)
gigamonSnmpOverThresholdChangeNotification.setObjects(
      *(("GIGAMON-SNMP-MIB", "gigamonSnmpNotifHardWareName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifLevel"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifDescription"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifPortName"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationAlarm"),
        ("GIGAMON-SNMP-MIB", "gigamonSnmpNotifUtilizationThreshold"))
)
if mibBuilder.loadTexts:
    gigamonSnmpOverThresholdChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GIGAMON-SNMP-MIB",
    **{"gigamonSnmp": gigamonSnmp,
       "gigamonSnmpNotifications": gigamonSnmpNotifications,
       "gigamonGigaVUE": gigamonGigaVUE,
       "gigamonSnmpResetSystemNotification": gigamonSnmpResetSystemNotification,
       "gigamonSnmpUserAuthFailNotification": gigamonSnmpUserAuthFailNotification,
       "gigamonSnmpFirmwareChangeNotification": gigamonSnmpFirmwareChangeNotification,
       "gigamonSnmpConfigSaveNotification": gigamonSnmpConfigSaveNotification,
       "gigamonSnmpModuleChangeNotification": gigamonSnmpModuleChangeNotification,
       "gigamonSnmpPacketDropNotification": gigamonSnmpPacketDropNotification,
       "gigamonSnmpTapRelayChangeNotification": gigamonSnmpTapRelayChangeNotification,
       "gigamonSnmpPortLinkChangeNotification": gigamonSnmpPortLinkChangeNotification,
       "gigamonSnmpRxTxErrorNotification": gigamonSnmpRxTxErrorNotification,
       "gigamonPowerChangeNotification": gigamonPowerChangeNotification,
       "gigamonFanChangeNotification": gigamonFanChangeNotification,
       "gigamonSnmpOverThresholdChangeNotification": gigamonSnmpOverThresholdChangeNotification,
       "gigamonSnmpNotificationObjects": gigamonSnmpNotificationObjects,
       "gigamonSnmpNotifLevel": gigamonSnmpNotifLevel,
       "gigamonSnmpNotifDescription": gigamonSnmpNotifDescription,
       "gigamonSnmpNotifOpType": gigamonSnmpNotifOpType,
       "gigamonSnmpNotifPortName": gigamonSnmpNotifPortName,
       "gigamonSnmpNotifPortLinkStatus": gigamonSnmpNotifPortLinkStatus,
       "gigamonSnmpNotifTAPRelayStatus": gigamonSnmpNotifTAPRelayStatus,
       "gigamonSnmpNotifRxTxType": gigamonSnmpNotifRxTxType,
       "gigamonSnmpNotifRxTxErrorType": gigamonSnmpNotifRxTxErrorType,
       "gigamonSnmpNotifCounter": gigamonSnmpNotifCounter,
       "gigamonSnmpNotifFirmwareName": gigamonSnmpNotifFirmwareName,
       "gigamonSnmpNotifModuleOperationType": gigamonSnmpNotifModuleOperationType,
       "gigamonSnmpNotifModuleName": gigamonSnmpNotifModuleName,
       "gigamonNotifSlotNumber": gigamonNotifSlotNumber,
       "gigamonSnmpNotifUserName": gigamonSnmpNotifUserName,
       "gigamonSnmpNotifFileName": gigamonSnmpNotifFileName,
       "gigamonNotifPowerStatus": gigamonNotifPowerStatus,
       "gigamonSnmpNotifHardWareName": gigamonSnmpNotifHardWareName,
       "gigamonSnmpNotifGigaVUE420SlotNumber": gigamonSnmpNotifGigaVUE420SlotNumber,
       "gigamonSnmpNotifFanName": gigamonSnmpNotifFanName,
       "gigamonNotifFanStatus": gigamonNotifFanStatus,
       "gigamonSnmpNotifUtilizationAlarm": gigamonSnmpNotifUtilizationAlarm,
       "gigamonSnmpNotifUtilizationThreshold": gigamonSnmpNotifUtilizationThreshold}
)

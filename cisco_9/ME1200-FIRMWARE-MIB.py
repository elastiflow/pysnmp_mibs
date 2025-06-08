# SNMP MIB module (ME1200-FIRMWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-FIRMWARE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:30 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString")

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


# MODULE-IDENTITY

me1200FirmwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28)
)
if mibBuilder.loadTexts:
    me1200FirmwareMIB.setRevisions(
        ("2014-12-16 00:00",
         "2014-02-18 00:00",
         "2014-01-29 00:00",
         "2014-01-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200StatusImageType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootloader", 0),
          ("activeFirmware", 1),
          ("alternativeFirmware", 2))
    )



class ME1200UploadImageType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bootloader", 0),
          ("firmware", 1))
    )



class ME1200UploadStatus(TextualConvention, Integer32):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("inProgress", 2),
          ("errIvalidIp", 3),
          ("errTftpFailed", 4),
          ("errBusy", 5),
          ("errMemoryInsufficient", 6),
          ("errInvalidImage", 7),
          ("errWriteFlash", 8),
          ("errSameImageExisted", 9),
          ("errUnknownImage", 10),
          ("errFlashImageNotFound", 11),
          ("errFlashEntryNotFound", 12),
          ("errCrc", 13),
          ("errImageSize", 14),
          ("errEraseFlash", 15),
          ("errIncorrectImageVersion", 16),
          ("errDownloadUrl", 17),
          ("errInvalidUrl", 18))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200FirmwareMIBObjects_ObjectIdentity = ObjectIdentity
me1200FirmwareMIBObjects = _Me1200FirmwareMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1)
)
_Me1200FirmwareStatus_ObjectIdentity = ObjectIdentity
me1200FirmwareStatus = _Me1200FirmwareStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3)
)
_Me1200FirmwareStatusImageTable_Object = MibTable
me1200FirmwareStatusImageTable = _Me1200FirmwareStatusImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageTable.setStatus("current")
_Me1200FirmwareStatusImageEntry_Object = MibTableRow
me1200FirmwareStatusImageEntry = _Me1200FirmwareStatusImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1)
)
me1200FirmwareStatusImageEntry.setIndexNames(
    (0, "ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageNumber"),
)
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageEntry.setStatus("current")


class _Me1200FirmwareStatusImageNumber_Type(Integer32):
    """Custom type me1200FirmwareStatusImageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Me1200FirmwareStatusImageNumber_Type.__name__ = "Integer32"
_Me1200FirmwareStatusImageNumber_Object = MibTableColumn
me1200FirmwareStatusImageNumber = _Me1200FirmwareStatusImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 1),
    _Me1200FirmwareStatusImageNumber_Type()
)
me1200FirmwareStatusImageNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageNumber.setStatus("current")
_Me1200FirmwareStatusImageType_Type = ME1200StatusImageType
_Me1200FirmwareStatusImageType_Object = MibTableColumn
me1200FirmwareStatusImageType = _Me1200FirmwareStatusImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 2),
    _Me1200FirmwareStatusImageType_Type()
)
me1200FirmwareStatusImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageType.setStatus("current")


class _Me1200FirmwareStatusImageName_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusImageName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Me1200FirmwareStatusImageName_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusImageName_Object = MibTableColumn
me1200FirmwareStatusImageName = _Me1200FirmwareStatusImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 3),
    _Me1200FirmwareStatusImageName_Type()
)
me1200FirmwareStatusImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageName.setStatus("current")


class _Me1200FirmwareStatusImageVersion_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusImageVersion based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200FirmwareStatusImageVersion_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusImageVersion_Object = MibTableColumn
me1200FirmwareStatusImageVersion = _Me1200FirmwareStatusImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 4),
    _Me1200FirmwareStatusImageVersion_Type()
)
me1200FirmwareStatusImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageVersion.setStatus("current")


class _Me1200FirmwareStatusImageBuiltDate_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusImageBuiltDate based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200FirmwareStatusImageBuiltDate_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusImageBuiltDate_Object = MibTableColumn
me1200FirmwareStatusImageBuiltDate = _Me1200FirmwareStatusImageBuiltDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 5),
    _Me1200FirmwareStatusImageBuiltDate_Type()
)
me1200FirmwareStatusImageBuiltDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageBuiltDate.setStatus("current")


class _Me1200FirmwareStatusImageCodeRevision_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusImageCodeRevision based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Me1200FirmwareStatusImageCodeRevision_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusImageCodeRevision_Object = MibTableColumn
me1200FirmwareStatusImageCodeRevision = _Me1200FirmwareStatusImageCodeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 1, 1, 6),
    _Me1200FirmwareStatusImageCodeRevision_Type()
)
me1200FirmwareStatusImageCodeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageCodeRevision.setStatus("current")
_Me1200FirmwareStatusImageUpload_ObjectIdentity = ObjectIdentity
me1200FirmwareStatusImageUpload = _Me1200FirmwareStatusImageUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 2)
)
_Me1200FirmwareStatusImageUploadStatus_Type = ME1200UploadStatus
_Me1200FirmwareStatusImageUploadStatus_Object = MibScalar
me1200FirmwareStatusImageUploadStatus = _Me1200FirmwareStatusImageUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 2, 1),
    _Me1200FirmwareStatusImageUploadStatus_Type()
)
me1200FirmwareStatusImageUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageUploadStatus.setStatus("current")
_Me1200FirmwareStatusSwitchTable_Object = MibTable
me1200FirmwareStatusSwitchTable = _Me1200FirmwareStatusSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchTable.setStatus("current")
_Me1200FirmwareStatusSwitchEntry_Object = MibTableRow
me1200FirmwareStatusSwitchEntry = _Me1200FirmwareStatusSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1)
)
me1200FirmwareStatusSwitchEntry.setIndexNames(
    (0, "ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchSwitchId"),
)
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchEntry.setStatus("current")


class _Me1200FirmwareStatusSwitchSwitchId_Type(Integer32):
    """Custom type me1200FirmwareStatusSwitchSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200FirmwareStatusSwitchSwitchId_Type.__name__ = "Integer32"
_Me1200FirmwareStatusSwitchSwitchId_Object = MibTableColumn
me1200FirmwareStatusSwitchSwitchId = _Me1200FirmwareStatusSwitchSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 1),
    _Me1200FirmwareStatusSwitchSwitchId_Type()
)
me1200FirmwareStatusSwitchSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchSwitchId.setStatus("current")


class _Me1200FirmwareStatusSwitchChipId_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusSwitchChipId based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Me1200FirmwareStatusSwitchChipId_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusSwitchChipId_Object = MibTableColumn
me1200FirmwareStatusSwitchChipId = _Me1200FirmwareStatusSwitchChipId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 2),
    _Me1200FirmwareStatusSwitchChipId_Type()
)
me1200FirmwareStatusSwitchChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchChipId.setStatus("current")


class _Me1200FirmwareStatusSwitchBoardType_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusSwitchBoardType based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Me1200FirmwareStatusSwitchBoardType_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusSwitchBoardType_Object = MibTableColumn
me1200FirmwareStatusSwitchBoardType = _Me1200FirmwareStatusSwitchBoardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 3),
    _Me1200FirmwareStatusSwitchBoardType_Type()
)
me1200FirmwareStatusSwitchBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchBoardType.setStatus("current")
_Me1200FirmwareStatusSwitchPortCnt_Type = Unsigned32
_Me1200FirmwareStatusSwitchPortCnt_Object = MibTableColumn
me1200FirmwareStatusSwitchPortCnt = _Me1200FirmwareStatusSwitchPortCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 4),
    _Me1200FirmwareStatusSwitchPortCnt_Type()
)
me1200FirmwareStatusSwitchPortCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchPortCnt.setStatus("current")


class _Me1200FirmwareStatusSwitchProduct_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusSwitchProduct based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Me1200FirmwareStatusSwitchProduct_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusSwitchProduct_Object = MibTableColumn
me1200FirmwareStatusSwitchProduct = _Me1200FirmwareStatusSwitchProduct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 5),
    _Me1200FirmwareStatusSwitchProduct_Type()
)
me1200FirmwareStatusSwitchProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchProduct.setStatus("current")


class _Me1200FirmwareStatusSwitchVersion_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusSwitchVersion based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200FirmwareStatusSwitchVersion_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusSwitchVersion_Object = MibTableColumn
me1200FirmwareStatusSwitchVersion = _Me1200FirmwareStatusSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 6),
    _Me1200FirmwareStatusSwitchVersion_Type()
)
me1200FirmwareStatusSwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchVersion.setStatus("current")


class _Me1200FirmwareStatusSwitchBuiltDate_Type(ME1200DisplayString):
    """Custom type me1200FirmwareStatusSwitchBuiltDate based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200FirmwareStatusSwitchBuiltDate_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareStatusSwitchBuiltDate_Object = MibTableColumn
me1200FirmwareStatusSwitchBuiltDate = _Me1200FirmwareStatusSwitchBuiltDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 3, 3, 1, 7),
    _Me1200FirmwareStatusSwitchBuiltDate_Type()
)
me1200FirmwareStatusSwitchBuiltDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchBuiltDate.setStatus("current")
_Me1200FirmwareControl_ObjectIdentity = ObjectIdentity
me1200FirmwareControl = _Me1200FirmwareControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4)
)
_Me1200FirmwareControlGlobals_ObjectIdentity = ObjectIdentity
me1200FirmwareControlGlobals = _Me1200FirmwareControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 1)
)
_Me1200FirmwareControlGlobalsSwapFirmware_Type = TruthValue
_Me1200FirmwareControlGlobalsSwapFirmware_Object = MibScalar
me1200FirmwareControlGlobalsSwapFirmware = _Me1200FirmwareControlGlobalsSwapFirmware_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 1, 1),
    _Me1200FirmwareControlGlobalsSwapFirmware_Type()
)
me1200FirmwareControlGlobalsSwapFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200FirmwareControlGlobalsSwapFirmware.setStatus("current")
_Me1200FirmwareControlImageUpload_ObjectIdentity = ObjectIdentity
me1200FirmwareControlImageUpload = _Me1200FirmwareControlImageUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2)
)
_Me1200FirmwareControlImageUploadDoUpload_Type = TruthValue
_Me1200FirmwareControlImageUploadDoUpload_Object = MibScalar
me1200FirmwareControlImageUploadDoUpload = _Me1200FirmwareControlImageUploadDoUpload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2, 1),
    _Me1200FirmwareControlImageUploadDoUpload_Type()
)
me1200FirmwareControlImageUploadDoUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200FirmwareControlImageUploadDoUpload.setStatus("current")
_Me1200FirmwareControlImageUploadImageType_Type = ME1200UploadImageType
_Me1200FirmwareControlImageUploadImageType_Object = MibScalar
me1200FirmwareControlImageUploadImageType = _Me1200FirmwareControlImageUploadImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2, 2),
    _Me1200FirmwareControlImageUploadImageType_Type()
)
me1200FirmwareControlImageUploadImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200FirmwareControlImageUploadImageType.setStatus("current")


class _Me1200FirmwareControlImageUploadUrl_Type(ME1200DisplayString):
    """Custom type me1200FirmwareControlImageUploadUrl based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Me1200FirmwareControlImageUploadUrl_Type.__name__ = "ME1200DisplayString"
_Me1200FirmwareControlImageUploadUrl_Object = MibScalar
me1200FirmwareControlImageUploadUrl = _Me1200FirmwareControlImageUploadUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 1, 4, 2, 3),
    _Me1200FirmwareControlImageUploadUrl_Type()
)
me1200FirmwareControlImageUploadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200FirmwareControlImageUploadUrl.setStatus("current")
_Me1200FirmwareMIBConformance_ObjectIdentity = ObjectIdentity
me1200FirmwareMIBConformance = _Me1200FirmwareMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2)
)
_Me1200FirmwareMIBCompliances_ObjectIdentity = ObjectIdentity
me1200FirmwareMIBCompliances = _Me1200FirmwareMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 1)
)
_Me1200FirmwareMIBGroups_ObjectIdentity = ObjectIdentity
me1200FirmwareMIBGroups = _Me1200FirmwareMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2)
)

# Managed Objects groups

me1200FirmwareStatusImageTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 1)
)
me1200FirmwareStatusImageTableInfoGroup.setObjects(
      *(("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageType"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageName"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageVersion"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageBuiltDate"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageCodeRevision"))
)
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageTableInfoGroup.setStatus("current")

me1200FirmwareStatusImageUploadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 2)
)
me1200FirmwareStatusImageUploadInfoGroup.setObjects(
    ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageUploadStatus")
)
if mibBuilder.loadTexts:
    me1200FirmwareStatusImageUploadInfoGroup.setStatus("current")

me1200FirmwareStatusSwitchTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 3)
)
me1200FirmwareStatusSwitchTableInfoGroup.setObjects(
      *(("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchChipId"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchBoardType"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchPortCnt"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchProduct"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchVersion"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchBuiltDate"))
)
if mibBuilder.loadTexts:
    me1200FirmwareStatusSwitchTableInfoGroup.setStatus("current")

me1200FirmwareControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 4)
)
me1200FirmwareControlGlobalsInfoGroup.setObjects(
    ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlGlobalsSwapFirmware")
)
if mibBuilder.loadTexts:
    me1200FirmwareControlGlobalsInfoGroup.setStatus("current")

me1200FirmwareControlImageUploadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 2, 5)
)
me1200FirmwareControlImageUploadInfoGroup.setObjects(
      *(("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadDoUpload"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadImageType"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadUrl"))
)
if mibBuilder.loadTexts:
    me1200FirmwareControlImageUploadInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200FirmwareMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 28, 2, 1, 1)
)
me1200FirmwareMIBCompliance.setObjects(
      *(("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageTableInfoGroup"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusImageUploadInfoGroup"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareStatusSwitchTableInfoGroup"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlGlobalsInfoGroup"),
        ("ME1200-FIRMWARE-MIB", "me1200FirmwareControlImageUploadInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200FirmwareMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-FIRMWARE-MIB",
    **{"ME1200StatusImageType": ME1200StatusImageType,
       "ME1200UploadImageType": ME1200UploadImageType,
       "ME1200UploadStatus": ME1200UploadStatus,
       "me1200FirmwareMIB": me1200FirmwareMIB,
       "me1200FirmwareMIBObjects": me1200FirmwareMIBObjects,
       "me1200FirmwareStatus": me1200FirmwareStatus,
       "me1200FirmwareStatusImageTable": me1200FirmwareStatusImageTable,
       "me1200FirmwareStatusImageEntry": me1200FirmwareStatusImageEntry,
       "me1200FirmwareStatusImageNumber": me1200FirmwareStatusImageNumber,
       "me1200FirmwareStatusImageType": me1200FirmwareStatusImageType,
       "me1200FirmwareStatusImageName": me1200FirmwareStatusImageName,
       "me1200FirmwareStatusImageVersion": me1200FirmwareStatusImageVersion,
       "me1200FirmwareStatusImageBuiltDate": me1200FirmwareStatusImageBuiltDate,
       "me1200FirmwareStatusImageCodeRevision": me1200FirmwareStatusImageCodeRevision,
       "me1200FirmwareStatusImageUpload": me1200FirmwareStatusImageUpload,
       "me1200FirmwareStatusImageUploadStatus": me1200FirmwareStatusImageUploadStatus,
       "me1200FirmwareStatusSwitchTable": me1200FirmwareStatusSwitchTable,
       "me1200FirmwareStatusSwitchEntry": me1200FirmwareStatusSwitchEntry,
       "me1200FirmwareStatusSwitchSwitchId": me1200FirmwareStatusSwitchSwitchId,
       "me1200FirmwareStatusSwitchChipId": me1200FirmwareStatusSwitchChipId,
       "me1200FirmwareStatusSwitchBoardType": me1200FirmwareStatusSwitchBoardType,
       "me1200FirmwareStatusSwitchPortCnt": me1200FirmwareStatusSwitchPortCnt,
       "me1200FirmwareStatusSwitchProduct": me1200FirmwareStatusSwitchProduct,
       "me1200FirmwareStatusSwitchVersion": me1200FirmwareStatusSwitchVersion,
       "me1200FirmwareStatusSwitchBuiltDate": me1200FirmwareStatusSwitchBuiltDate,
       "me1200FirmwareControl": me1200FirmwareControl,
       "me1200FirmwareControlGlobals": me1200FirmwareControlGlobals,
       "me1200FirmwareControlGlobalsSwapFirmware": me1200FirmwareControlGlobalsSwapFirmware,
       "me1200FirmwareControlImageUpload": me1200FirmwareControlImageUpload,
       "me1200FirmwareControlImageUploadDoUpload": me1200FirmwareControlImageUploadDoUpload,
       "me1200FirmwareControlImageUploadImageType": me1200FirmwareControlImageUploadImageType,
       "me1200FirmwareControlImageUploadUrl": me1200FirmwareControlImageUploadUrl,
       "me1200FirmwareMIBConformance": me1200FirmwareMIBConformance,
       "me1200FirmwareMIBCompliances": me1200FirmwareMIBCompliances,
       "me1200FirmwareMIBCompliance": me1200FirmwareMIBCompliance,
       "me1200FirmwareMIBGroups": me1200FirmwareMIBGroups,
       "me1200FirmwareStatusImageTableInfoGroup": me1200FirmwareStatusImageTableInfoGroup,
       "me1200FirmwareStatusImageUploadInfoGroup": me1200FirmwareStatusImageUploadInfoGroup,
       "me1200FirmwareStatusSwitchTableInfoGroup": me1200FirmwareStatusSwitchTableInfoGroup,
       "me1200FirmwareControlGlobalsInfoGroup": me1200FirmwareControlGlobalsInfoGroup,
       "me1200FirmwareControlImageUploadInfoGroup": me1200FirmwareControlImageUploadInfoGroup}
)

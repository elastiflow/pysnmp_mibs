# SNMP MIB module (AIRCELL-ABS-CLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aircell_28382/AIRCELL-ABS-CLD-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:18:40 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aircellAbsCldMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 4)
)
if mibBuilder.loadTexts:
    aircellAbsCldMib.setRevisions(
        ("2009-08-17 14:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aircell_ObjectIdentity = ObjectIdentity
aircell = _Aircell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382)
)
_Cld_ObjectIdentity = ObjectIdentity
cld = _Cld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1)
)


class _AbsCldOperStatus_Type(Integer32):
    """Custom type absCldOperStatus based on Integer32"""
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


_AbsCldOperStatus_Type.__name__ = "Integer32"
_AbsCldOperStatus_Object = MibScalar
absCldOperStatus = _AbsCldOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 1),
    _AbsCldOperStatus_Type()
)
absCldOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldOperStatus.setStatus("current")


class _AbsCldDeviceReset_Type(Integer32):
    """Custom type absCldDeviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noreset", 0),
          ("resetdevice", 1))
    )


_AbsCldDeviceReset_Type.__name__ = "Integer32"
_AbsCldDeviceReset_Object = MibScalar
absCldDeviceReset = _AbsCldDeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 2),
    _AbsCldDeviceReset_Type()
)
absCldDeviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absCldDeviceReset.setStatus("current")
_AbsCldTrapMgrIpAddr_Type = IpAddress
_AbsCldTrapMgrIpAddr_Object = MibScalar
absCldTrapMgrIpAddr = _AbsCldTrapMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 3),
    _AbsCldTrapMgrIpAddr_Type()
)
absCldTrapMgrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldTrapMgrIpAddr.setStatus("current")
_AbsCldHWPartNumber_Type = DisplayString
_AbsCldHWPartNumber_Object = MibScalar
absCldHWPartNumber = _AbsCldHWPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 4),
    _AbsCldHWPartNumber_Type()
)
absCldHWPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldHWPartNumber.setStatus("current")
_AbsCldSWPartNumber_Type = DisplayString
_AbsCldSWPartNumber_Object = MibScalar
absCldSWPartNumber = _AbsCldSWPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 5),
    _AbsCldSWPartNumber_Type()
)
absCldSWPartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absCldSWPartNumber.setStatus("current")


class _AbsCldUsbAdminStatus_Type(Integer32):
    """Custom type absCldUsbAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )


_AbsCldUsbAdminStatus_Type.__name__ = "Integer32"
_AbsCldUsbAdminStatus_Object = MibScalar
absCldUsbAdminStatus = _AbsCldUsbAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 6),
    _AbsCldUsbAdminStatus_Type()
)
absCldUsbAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absCldUsbAdminStatus.setStatus("current")
_AbsCldTime_Type = DisplayString
_AbsCldTime_Object = MibScalar
absCldTime = _AbsCldTime_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 7),
    _AbsCldTime_Type()
)
absCldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absCldTime.setStatus("current")
_CldUsbTable_Object = MibTable
cldUsbTable = _CldUsbTable_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 8)
)
if mibBuilder.loadTexts:
    cldUsbTable.setStatus("current")
_CldUsbEntry_Object = MibTableRow
cldUsbEntry = _CldUsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 8, 1)
)
cldUsbEntry.setIndexNames(
    (0, "AIRCELL-ABS-CLD-MIB", "usbNumber"),
)
if mibBuilder.loadTexts:
    cldUsbEntry.setStatus("current")


class _UsbNumber_Type(Integer32):
    """Custom type usbNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UsbNumber_Type.__name__ = "Integer32"
_UsbNumber_Object = MibTableColumn
usbNumber = _UsbNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 8, 1, 1),
    _UsbNumber_Type()
)
usbNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usbNumber.setStatus("current")
_UsbSerialNumber_Type = DisplayString
_UsbSerialNumber_Object = MibTableColumn
usbSerialNumber = _UsbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 8, 1, 2),
    _UsbSerialNumber_Type()
)
usbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbSerialNumber.setStatus("current")
_UsbMountPath_Type = DisplayString
_UsbMountPath_Object = MibTableColumn
usbMountPath = _UsbMountPath_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 8, 1, 3),
    _UsbMountPath_Type()
)
usbMountPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbMountPath.setStatus("current")


class _UsbStatus_Type(Integer32):
    """Custom type usbStatus based on Integer32"""
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
        *(("active", 1),
          ("validationFailure", 2),
          ("mountFailure", 3),
          ("notReady", 4))
    )


_UsbStatus_Type.__name__ = "Integer32"
_UsbStatus_Object = MibTableColumn
usbStatus = _UsbStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 8, 1, 4),
    _UsbStatus_Type()
)
usbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbStatus.setStatus("current")
_UsbDeviceName_Type = DisplayString
_UsbDeviceName_Object = MibTableColumn
usbDeviceName = _UsbDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 1, 8, 1, 5),
    _UsbDeviceName_Type()
)
usbDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usbDeviceName.setStatus("current")
_CldSWDownload_ObjectIdentity = ObjectIdentity
cldSWDownload = _CldSWDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 4, 2)
)


class _AbsCldSWDownloadControl_Type(Integer32):
    """Custom type absCldSWDownloadControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableKernel", 2),
          ("enableFileSystem", 3))
    )


_AbsCldSWDownloadControl_Type.__name__ = "Integer32"
_AbsCldSWDownloadControl_Object = MibScalar
absCldSWDownloadControl = _AbsCldSWDownloadControl_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 2, 1),
    _AbsCldSWDownloadControl_Type()
)
absCldSWDownloadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absCldSWDownloadControl.setStatus("current")


class _AbsCldSWDownloadStatus_Type(Integer32):
    """Custom type absCldSWDownloadStatus based on Integer32"""
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
          ("kernelDownloadSuccess", 2),
          ("fileSystemDownloadSuccess", 3),
          ("kernelDownloadFailed", 4),
          ("fileSystemDownloadFailed", 5),
          ("kernelDownloadInProgress", 6),
          ("fileSystemDownloadInProgress", 7))
    )


_AbsCldSWDownloadStatus_Type.__name__ = "Integer32"
_AbsCldSWDownloadStatus_Object = MibScalar
absCldSWDownloadStatus = _AbsCldSWDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 2, 2),
    _AbsCldSWDownloadStatus_Type()
)
absCldSWDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldSWDownloadStatus.setStatus("current")
_AbsCldSWDownloadKernelVersion_Type = DisplayString
_AbsCldSWDownloadKernelVersion_Object = MibScalar
absCldSWDownloadKernelVersion = _AbsCldSWDownloadKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 2, 3),
    _AbsCldSWDownloadKernelVersion_Type()
)
absCldSWDownloadKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldSWDownloadKernelVersion.setStatus("current")
_AbsCldSWDownloadFileSystemVersion_Type = DisplayString
_AbsCldSWDownloadFileSystemVersion_Object = MibScalar
absCldSWDownloadFileSystemVersion = _AbsCldSWDownloadFileSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 2, 4),
    _AbsCldSWDownloadFileSystemVersion_Type()
)
absCldSWDownloadFileSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldSWDownloadFileSystemVersion.setStatus("current")
_AbsCldSWDownloadTFTPIpAddress_Type = IpAddress
_AbsCldSWDownloadTFTPIpAddress_Object = MibScalar
absCldSWDownloadTFTPIpAddress = _AbsCldSWDownloadTFTPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 2, 5),
    _AbsCldSWDownloadTFTPIpAddress_Type()
)
absCldSWDownloadTFTPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absCldSWDownloadTFTPIpAddress.setStatus("current")


class _AbsCldSWImageType_Type(Integer32):
    """Custom type absCldSWImageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fallback", 2))
    )


_AbsCldSWImageType_Type.__name__ = "Integer32"
_AbsCldSWImageType_Object = MibScalar
absCldSWImageType = _AbsCldSWImageType_Object(
    (1, 3, 6, 1, 4, 1, 28382, 4, 2, 6),
    _AbsCldSWImageType_Type()
)
absCldSWImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCldSWImageType.setStatus("current")
_CldCompliances_ObjectIdentity = ObjectIdentity
cldCompliances = _CldCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 4, 3)
)
_CldGroups_ObjectIdentity = ObjectIdentity
cldGroups = _CldGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 4, 4)
)

# Managed Objects groups

cldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28382, 4, 4, 1)
)
cldGroup.setObjects(
      *(("AIRCELL-ABS-CLD-MIB", "absCldOperStatus"),
        ("AIRCELL-ABS-CLD-MIB", "absCldDeviceReset"),
        ("AIRCELL-ABS-CLD-MIB", "absCldTrapMgrIpAddr"),
        ("AIRCELL-ABS-CLD-MIB", "absCldHWPartNumber"),
        ("AIRCELL-ABS-CLD-MIB", "absCldSWPartNumber"),
        ("AIRCELL-ABS-CLD-MIB", "absCldTime"),
        ("AIRCELL-ABS-CLD-MIB", "absCldUsbAdminStatus"),
        ("AIRCELL-ABS-CLD-MIB", "usbSerialNumber"),
        ("AIRCELL-ABS-CLD-MIB", "usbMountPath"),
        ("AIRCELL-ABS-CLD-MIB", "usbStatus"),
        ("AIRCELL-ABS-CLD-MIB", "usbDeviceName"),
        ("AIRCELL-ABS-CLD-MIB", "absCldSWDownloadControl"),
        ("AIRCELL-ABS-CLD-MIB", "absCldSWDownloadStatus"),
        ("AIRCELL-ABS-CLD-MIB", "absCldSWDownloadKernelVersion"),
        ("AIRCELL-ABS-CLD-MIB", "absCldSWDownloadFileSystemVersion"),
        ("AIRCELL-ABS-CLD-MIB", "absCldSWDownloadTFTPIpAddress"),
        ("AIRCELL-ABS-CLD-MIB", "absCldSWImageType"))
)
if mibBuilder.loadTexts:
    cldGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28382, 4, 3, 1)
)
cldCompliance.setObjects(
    ("AIRCELL-ABS-CLD-MIB", "cldGroup")
)
if mibBuilder.loadTexts:
    cldCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRCELL-ABS-CLD-MIB",
    **{"aircell": aircell,
       "aircellAbsCldMib": aircellAbsCldMib,
       "cld": cld,
       "absCldOperStatus": absCldOperStatus,
       "absCldDeviceReset": absCldDeviceReset,
       "absCldTrapMgrIpAddr": absCldTrapMgrIpAddr,
       "absCldHWPartNumber": absCldHWPartNumber,
       "absCldSWPartNumber": absCldSWPartNumber,
       "absCldUsbAdminStatus": absCldUsbAdminStatus,
       "absCldTime": absCldTime,
       "cldUsbTable": cldUsbTable,
       "cldUsbEntry": cldUsbEntry,
       "usbNumber": usbNumber,
       "usbSerialNumber": usbSerialNumber,
       "usbMountPath": usbMountPath,
       "usbStatus": usbStatus,
       "usbDeviceName": usbDeviceName,
       "cldSWDownload": cldSWDownload,
       "absCldSWDownloadControl": absCldSWDownloadControl,
       "absCldSWDownloadStatus": absCldSWDownloadStatus,
       "absCldSWDownloadKernelVersion": absCldSWDownloadKernelVersion,
       "absCldSWDownloadFileSystemVersion": absCldSWDownloadFileSystemVersion,
       "absCldSWDownloadTFTPIpAddress": absCldSWDownloadTFTPIpAddress,
       "absCldSWImageType": absCldSWImageType,
       "cldCompliances": cldCompliances,
       "cldCompliance": cldCompliance,
       "cldGroups": cldGroups,
       "cldGroup": cldGroup}
)

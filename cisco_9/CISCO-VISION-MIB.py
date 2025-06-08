# SNMP MIB module (CISCO-VISION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-VISION-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:02:39 2025
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

ciscoVisionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051)
)
if mibBuilder.loadTexts:
    ciscoVisionMIB.setRevisions(
        ("2021-02-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVisionMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVisionMIBNotifs = _CiscoVisionMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 0)
)
_CiscoVisionMIBConform_ObjectIdentity = ObjectIdentity
ciscoVisionMIBConform = _CiscoVisionMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1)
)
_CiscoVisionMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVisionMIBCompliances = _CiscoVisionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 1)
)
_CiscoVisionMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVisionMIBGroups = _CiscoVisionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 2)
)
_CiscoVisionDsd_ObjectIdentity = ObjectIdentity
ciscoVisionDsd = _CiscoVisionDsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2)
)
_CiscoVdService_ObjectIdentity = ObjectIdentity
ciscoVdService = _CiscoVdService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 1)
)
_CiscoVdServiceTable_Object = MibTable
ciscoVdServiceTable = _CiscoVdServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVdServiceTable.setStatus("current")
_CiscoVdServiceEntry_Object = MibTableRow
ciscoVdServiceEntry = _CiscoVdServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 1, 1, 1)
)
ciscoVdServiceEntry.setIndexNames(
    (0, "CISCO-VISION-MIB", "ciscoVdDsdServiceName"),
)
if mibBuilder.loadTexts:
    ciscoVdServiceEntry.setStatus("current")


class _CiscoVdDsdServiceName_Type(DisplayString):
    """Custom type ciscoVdDsdServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CiscoVdDsdServiceName_Type.__name__ = "DisplayString"
_CiscoVdDsdServiceName_Object = MibTableColumn
ciscoVdDsdServiceName = _CiscoVdDsdServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 1, 1, 1, 1),
    _CiscoVdDsdServiceName_Type()
)
ciscoVdDsdServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdDsdServiceName.setStatus("current")


class _CiscoVdDsdServiceStatus_Type(Integer32):
    """Custom type ciscoVdDsdServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVdDsdServiceStatus_Type.__name__ = "Integer32"
_CiscoVdDsdServiceStatus_Object = MibTableColumn
ciscoVdDsdServiceStatus = _CiscoVdDsdServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 1, 1, 1, 2),
    _CiscoVdDsdServiceStatus_Type()
)
ciscoVdDsdServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdDsdServiceStatus.setStatus("current")
_CiscoVdDsdServiceDesc_Type = DisplayString
_CiscoVdDsdServiceDesc_Object = MibTableColumn
ciscoVdDsdServiceDesc = _CiscoVdDsdServiceDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 1, 1, 1, 3),
    _CiscoVdDsdServiceDesc_Type()
)
ciscoVdDsdServiceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdDsdServiceDesc.setStatus("current")
_CiscoVdDmpsStatuses_ObjectIdentity = ObjectIdentity
ciscoVdDmpsStatuses = _CiscoVdDmpsStatuses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 2)
)
_CiscoVdDmpStatusTable_Object = MibTable
ciscoVdDmpStatusTable = _CiscoVdDmpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoVdDmpStatusTable.setStatus("current")
_CiscoVdDmpStatusEntry_Object = MibTableRow
ciscoVdDmpStatusEntry = _CiscoVdDmpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 2, 1, 1)
)
ciscoVdDmpStatusEntry.setIndexNames(
    (0, "CISCO-VISION-MIB", "ciscoVdDmpIP"),
)
if mibBuilder.loadTexts:
    ciscoVdDmpStatusEntry.setStatus("current")
_CiscoVdDmpIP_Type = IpAddress
_CiscoVdDmpIP_Object = MibTableColumn
ciscoVdDmpIP = _CiscoVdDmpIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 2, 1, 1, 1),
    _CiscoVdDmpIP_Type()
)
ciscoVdDmpIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoVdDmpIP.setStatus("current")


class _CiscoVdHdmiUpDownStatus_Type(Integer32):
    """Custom type ciscoVdHdmiUpDownStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVdHdmiUpDownStatus_Type.__name__ = "Integer32"
_CiscoVdHdmiUpDownStatus_Object = MibTableColumn
ciscoVdHdmiUpDownStatus = _CiscoVdHdmiUpDownStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 2, 1, 1, 2),
    _CiscoVdHdmiUpDownStatus_Type()
)
ciscoVdHdmiUpDownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdHdmiUpDownStatus.setStatus("current")


class _CiscoVdDmpStatus_Type(Integer32):
    """Custom type ciscoVdDmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVdDmpStatus_Type.__name__ = "Integer32"
_CiscoVdDmpStatus_Object = MibTableColumn
ciscoVdDmpStatus = _CiscoVdDmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 2, 1, 1, 3),
    _CiscoVdDmpStatus_Type()
)
ciscoVdDmpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdDmpStatus.setStatus("current")


class _CiscoVdDmpidentifier_Type(DisplayString):
    """Custom type ciscoVdDmpidentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoVdDmpidentifier_Type.__name__ = "DisplayString"
_CiscoVdDmpidentifier_Object = MibTableColumn
ciscoVdDmpidentifier = _CiscoVdDmpidentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 2, 1, 1, 4),
    _CiscoVdDmpidentifier_Type()
)
ciscoVdDmpidentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVdDmpidentifier.setStatus("current")


class _CiscoVdNtpSyncStatus_Type(Integer32):
    """Custom type ciscoVdNtpSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVdNtpSyncStatus_Type.__name__ = "Integer32"
_CiscoVdNtpSyncStatus_Object = MibScalar
ciscoVdNtpSyncStatus = _CiscoVdNtpSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 3),
    _CiscoVdNtpSyncStatus_Type()
)
ciscoVdNtpSyncStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoVdNtpSyncStatus.setStatus("current")


class _CiscoVdBkpStatus_Type(Integer32):
    """Custom type ciscoVdBkpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVdBkpStatus_Type.__name__ = "Integer32"
_CiscoVdBkpStatus_Object = MibScalar
ciscoVdBkpStatus = _CiscoVdBkpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 2, 4),
    _CiscoVdBkpStatus_Type()
)
ciscoVdBkpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoVdBkpStatus.setStatus("current")
_CiscoVisionDmp_ObjectIdentity = ObjectIdentity
ciscoVisionDmp = _CiscoVisionDmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3)
)


class _CiscoVisionDmpTvOnOff_Type(Integer32):
    """Custom type ciscoVisionDmpTvOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVisionDmpTvOnOff_Type.__name__ = "Integer32"
_CiscoVisionDmpTvOnOff_Object = MibScalar
ciscoVisionDmpTvOnOff = _CiscoVisionDmpTvOnOff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 1),
    _CiscoVisionDmpTvOnOff_Type()
)
ciscoVisionDmpTvOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpTvOnOff.setStatus("current")


class _CiscoVisionDmpNtpStatus_Type(Integer32):
    """Custom type ciscoVisionDmpNtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVisionDmpNtpStatus_Type.__name__ = "Integer32"
_CiscoVisionDmpNtpStatus_Object = MibScalar
ciscoVisionDmpNtpStatus = _CiscoVisionDmpNtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 2),
    _CiscoVisionDmpNtpStatus_Type()
)
ciscoVisionDmpNtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpNtpStatus.setStatus("current")
_CiscoVisionDmpPTP_ObjectIdentity = ObjectIdentity
ciscoVisionDmpPTP = _CiscoVisionDmpPTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 3)
)


class _CiscoVisionDmpPTPstatus_Type(Integer32):
    """Custom type ciscoVisionDmpPTPstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVisionDmpPTPstatus_Type.__name__ = "Integer32"
_CiscoVisionDmpPTPstatus_Object = MibScalar
ciscoVisionDmpPTPstatus = _CiscoVisionDmpPTPstatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 3, 1),
    _CiscoVisionDmpPTPstatus_Type()
)
ciscoVisionDmpPTPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpPTPstatus.setStatus("current")


class _CiscoVisionDmpPTPMaster_Type(Integer32):
    """Custom type ciscoVisionDmpPTPMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_CiscoVisionDmpPTPMaster_Type.__name__ = "Integer32"
_CiscoVisionDmpPTPMaster_Object = MibScalar
ciscoVisionDmpPTPMaster = _CiscoVisionDmpPTPMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 3, 2),
    _CiscoVisionDmpPTPMaster_Type()
)
ciscoVisionDmpPTPMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpPTPMaster.setStatus("current")


class _CiscoVisionDmpPTPDeviation_Type(DisplayString):
    """Custom type ciscoVisionDmpPTPDeviation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoVisionDmpPTPDeviation_Type.__name__ = "DisplayString"
_CiscoVisionDmpPTPDeviation_Object = MibScalar
ciscoVisionDmpPTPDeviation = _CiscoVisionDmpPTPDeviation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 3, 3),
    _CiscoVisionDmpPTPDeviation_Type()
)
ciscoVisionDmpPTPDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpPTPDeviation.setStatus("current")
_CiscoVisionNetwork_ObjectIdentity = ObjectIdentity
ciscoVisionNetwork = _CiscoVisionNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 4)
)


class _CiscoVisionDmpInterfaceDesc_Type(DisplayString):
    """Custom type ciscoVisionDmpInterfaceDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CiscoVisionDmpInterfaceDesc_Type.__name__ = "DisplayString"
_CiscoVisionDmpInterfaceDesc_Object = MibScalar
ciscoVisionDmpInterfaceDesc = _CiscoVisionDmpInterfaceDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 4, 1),
    _CiscoVisionDmpInterfaceDesc_Type()
)
ciscoVisionDmpInterfaceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpInterfaceDesc.setStatus("current")
_CiscoVisionDmpBytesIn_Type = Integer32
_CiscoVisionDmpBytesIn_Object = MibScalar
ciscoVisionDmpBytesIn = _CiscoVisionDmpBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 4, 2),
    _CiscoVisionDmpBytesIn_Type()
)
ciscoVisionDmpBytesIn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoVisionDmpBytesIn.setStatus("current")
_CiscoVisionDmpBytesOut_Type = Integer32
_CiscoVisionDmpBytesOut_Object = MibScalar
ciscoVisionDmpBytesOut = _CiscoVisionDmpBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 4, 3),
    _CiscoVisionDmpBytesOut_Type()
)
ciscoVisionDmpBytesOut.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoVisionDmpBytesOut.setStatus("current")
_CiscoVisionDmpPktCnt_Type = Integer32
_CiscoVisionDmpPktCnt_Object = MibScalar
ciscoVisionDmpPktCnt = _CiscoVisionDmpPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 4, 4),
    _CiscoVisionDmpPktCnt_Type()
)
ciscoVisionDmpPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpPktCnt.setStatus("current")
_CiscoVisionDmpPktErrCnt_Type = Integer32
_CiscoVisionDmpPktErrCnt_Object = MibScalar
ciscoVisionDmpPktErrCnt = _CiscoVisionDmpPktErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 4, 5),
    _CiscoVisionDmpPktErrCnt_Type()
)
ciscoVisionDmpPktErrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoVisionDmpPktErrCnt.setStatus("current")
_CiscoVisionDmpCpu_ObjectIdentity = ObjectIdentity
ciscoVisionDmpCpu = _CiscoVisionDmpCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 5)
)
_SsCpuRawUser_Type = Integer32
_SsCpuRawUser_Object = MibScalar
ssCpuRawUser = _SsCpuRawUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 5, 1),
    _SsCpuRawUser_Type()
)
ssCpuRawUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawUser.setStatus("current")
_SsCpuRawIdle_Type = Integer32
_SsCpuRawIdle_Object = MibScalar
ssCpuRawIdle = _SsCpuRawIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 3, 5, 2),
    _SsCpuRawIdle_Type()
)
ssCpuRawIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawIdle.setStatus("current")

# Managed Objects groups

ciscoVisiondsdSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 2, 1)
)
ciscoVisiondsdSvcGroup.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVdDsdServiceStatus"),
        ("CISCO-VISION-MIB", "ciscoVdNtpSyncStatus"),
        ("CISCO-VISION-MIB", "ciscoVdBkpStatus"),
        ("CISCO-VISION-MIB", "ciscoVdDsdServiceDesc"))
)
if mibBuilder.loadTexts:
    ciscoVisiondsdSvcGroup.setStatus("current")

ciscoVisiondsdDmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 2, 3)
)
ciscoVisiondsdDmpGroup.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVdHdmiUpDownStatus"),
        ("CISCO-VISION-MIB", "ciscoVdDmpStatus"),
        ("CISCO-VISION-MIB", "ciscoVdDmpidentifier"))
)
if mibBuilder.loadTexts:
    ciscoVisiondsdDmpGroup.setStatus("current")

ciscoVisionDmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 2, 4)
)
ciscoVisionDmpGroup.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVisionDmpTvOnOff"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpNtpStatus"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpPTPstatus"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpPTPMaster"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpPTPDeviation"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpInterfaceDesc"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpBytesIn"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpBytesOut"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpPktCnt"),
        ("CISCO-VISION-MIB", "ciscoVisionDmpPktErrCnt"),
        ("CISCO-VISION-MIB", "ssCpuRawUser"),
        ("CISCO-VISION-MIB", "ssCpuRawIdle"))
)
if mibBuilder.loadTexts:
    ciscoVisionDmpGroup.setStatus("current")


# Notification objects

ciscoVdServiceStatusNotifs = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 0, 1)
)
ciscoVdServiceStatusNotifs.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVdDsdServiceStatus"),
        ("CISCO-VISION-MIB", "ciscoVdDsdServiceDesc"))
)
if mibBuilder.loadTexts:
    ciscoVdServiceStatusNotifs.setStatus(
        "current"
    )

ciscoVdBackupTaskNotifs = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 0, 2)
)
ciscoVdBackupTaskNotifs.setObjects(
    ("CISCO-VISION-MIB", "ciscoVdBkpStatus")
)
if mibBuilder.loadTexts:
    ciscoVdBackupTaskNotifs.setStatus(
        "current"
    )

ciscoVdNtpNotifs = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 0, 3)
)
ciscoVdNtpNotifs.setObjects(
    ("CISCO-VISION-MIB", "ciscoVdNtpSyncStatus")
)
if mibBuilder.loadTexts:
    ciscoVdNtpNotifs.setStatus(
        "current"
    )

ciscoVdHdmiUpDwnNotifs = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 0, 4)
)
ciscoVdHdmiUpDwnNotifs.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVdHdmiUpDownStatus"),
        ("CISCO-VISION-MIB", "ciscoVdDmpidentifier"))
)
if mibBuilder.loadTexts:
    ciscoVdHdmiUpDwnNotifs.setStatus(
        "current"
    )


# Notifications groups

ciscoVisiondsdMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 2, 2)
)
ciscoVisiondsdMIBNotifsGroup.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVdServiceStatusNotifs"),
        ("CISCO-VISION-MIB", "ciscoVdBackupTaskNotifs"),
        ("CISCO-VISION-MIB", "ciscoVdNtpNotifs"),
        ("CISCO-VISION-MIB", "ciscoVdHdmiUpDwnNotifs"))
)
if mibBuilder.loadTexts:
    ciscoVisiondsdMIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoVisionDsdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 1, 1)
)
ciscoVisionDsdMIBCompliance.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVisiondsdSvcGroup"),
        ("CISCO-VISION-MIB", "ciscoVisiondsdDmpGroup"),
        ("CISCO-VISION-MIB", "ciscoVisiondsdMIBNotifsGroup"))
)
if mibBuilder.loadTexts:
    ciscoVisionDsdMIBCompliance.setStatus(
        "current"
    )

ciscoVisionDmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1051, 1, 1, 2)
)
ciscoVisionDmpMIBCompliance.setObjects(
      *(("CISCO-VISION-MIB", "ciscoVisionDmpGroup"),
        ("CISCO-VISION-MIB", "ciscoVisiondsdSvcGroup"),
        ("CISCO-VISION-MIB", "ciscoVisiondsdMIBNotifsGroup"),
        ("CISCO-VISION-MIB", "ciscoVisiondsdDmpGroup"))
)
if mibBuilder.loadTexts:
    ciscoVisionDmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISION-MIB",
    **{"ciscoVisionMIB": ciscoVisionMIB,
       "ciscoVisionMIBNotifs": ciscoVisionMIBNotifs,
       "ciscoVdServiceStatusNotifs": ciscoVdServiceStatusNotifs,
       "ciscoVdBackupTaskNotifs": ciscoVdBackupTaskNotifs,
       "ciscoVdNtpNotifs": ciscoVdNtpNotifs,
       "ciscoVdHdmiUpDwnNotifs": ciscoVdHdmiUpDwnNotifs,
       "ciscoVisionMIBConform": ciscoVisionMIBConform,
       "ciscoVisionMIBCompliances": ciscoVisionMIBCompliances,
       "ciscoVisionDsdMIBCompliance": ciscoVisionDsdMIBCompliance,
       "ciscoVisionDmpMIBCompliance": ciscoVisionDmpMIBCompliance,
       "ciscoVisionMIBGroups": ciscoVisionMIBGroups,
       "ciscoVisiondsdSvcGroup": ciscoVisiondsdSvcGroup,
       "ciscoVisiondsdMIBNotifsGroup": ciscoVisiondsdMIBNotifsGroup,
       "ciscoVisiondsdDmpGroup": ciscoVisiondsdDmpGroup,
       "ciscoVisionDmpGroup": ciscoVisionDmpGroup,
       "ciscoVisionDsd": ciscoVisionDsd,
       "ciscoVdService": ciscoVdService,
       "ciscoVdServiceTable": ciscoVdServiceTable,
       "ciscoVdServiceEntry": ciscoVdServiceEntry,
       "ciscoVdDsdServiceName": ciscoVdDsdServiceName,
       "ciscoVdDsdServiceStatus": ciscoVdDsdServiceStatus,
       "ciscoVdDsdServiceDesc": ciscoVdDsdServiceDesc,
       "ciscoVdDmpsStatuses": ciscoVdDmpsStatuses,
       "ciscoVdDmpStatusTable": ciscoVdDmpStatusTable,
       "ciscoVdDmpStatusEntry": ciscoVdDmpStatusEntry,
       "ciscoVdDmpIP": ciscoVdDmpIP,
       "ciscoVdHdmiUpDownStatus": ciscoVdHdmiUpDownStatus,
       "ciscoVdDmpStatus": ciscoVdDmpStatus,
       "ciscoVdDmpidentifier": ciscoVdDmpidentifier,
       "ciscoVdNtpSyncStatus": ciscoVdNtpSyncStatus,
       "ciscoVdBkpStatus": ciscoVdBkpStatus,
       "ciscoVisionDmp": ciscoVisionDmp,
       "ciscoVisionDmpTvOnOff": ciscoVisionDmpTvOnOff,
       "ciscoVisionDmpNtpStatus": ciscoVisionDmpNtpStatus,
       "ciscoVisionDmpPTP": ciscoVisionDmpPTP,
       "ciscoVisionDmpPTPstatus": ciscoVisionDmpPTPstatus,
       "ciscoVisionDmpPTPMaster": ciscoVisionDmpPTPMaster,
       "ciscoVisionDmpPTPDeviation": ciscoVisionDmpPTPDeviation,
       "ciscoVisionNetwork": ciscoVisionNetwork,
       "ciscoVisionDmpInterfaceDesc": ciscoVisionDmpInterfaceDesc,
       "ciscoVisionDmpBytesIn": ciscoVisionDmpBytesIn,
       "ciscoVisionDmpBytesOut": ciscoVisionDmpBytesOut,
       "ciscoVisionDmpPktCnt": ciscoVisionDmpPktCnt,
       "ciscoVisionDmpPktErrCnt": ciscoVisionDmpPktErrCnt,
       "ciscoVisionDmpCpu": ciscoVisionDmpCpu,
       "ssCpuRawUser": ssCpuRawUser,
       "ssCpuRawIdle": ssCpuRawIdle}
)

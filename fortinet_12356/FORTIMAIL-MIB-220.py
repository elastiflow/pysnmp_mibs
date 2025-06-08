# SNMP MIB module (FORTIMAIL-MIB-220) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fortinet_12356/FORTIMAIL-MIB-220.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:36:31 2025
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


# Types definitions



class FmlBoolState(Integer32):
    """Custom type FmlBoolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )





class FmlIndex(Integer32):
    """Custom type FmlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class FmlOpMode(Integer32):
    """Custom type FmlOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 1),
          ("transparent", 2),
          ("server", 3))
    )





class FmlSessProto(Integer32):
    """Custom type FmlSessProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              89,
              103,
              108,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ipip", 4),
          ("tcp", 6),
          ("egp", 8),
          ("pup", 12),
          ("udp", 17),
          ("idp", 22),
          ("ipv6", 41),
          ("rsvp", 46),
          ("gre", 47),
          ("esp", 50),
          ("ah", 51),
          ("ospf", 89),
          ("pim", 103),
          ("comp", 108),
          ("raw", 255))
    )





class FmlLanguageCode(Integer32):
    """Custom type FmlLanguageCode based on Integer32"""
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
        *(("western", 1),
          ("simplifiedChinese", 2),
          ("traditionalChinese", 3),
          ("japanese", 4),
          ("kerean", 5),
          ("default", 6))
    )





class FmlSysEventCode(Integer32):
    """Custom type FmlSysEventCode based on Integer32"""
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
        *(("systemHalt", 1),
          ("systemReboot", 2),
          ("systemReload", 3),
          ("systemUpgrade", 4),
          ("guiUpgrade", 5),
          ("logdiskFormat", 6),
          ("maildiskFormat", 7),
          ("AVDBUpdate", 8))
    )





class FmlRAIDCode(Integer32):
    """Custom type FmlRAIDCode based on Integer32"""
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
        *(("DegradedArray", 1),
          ("SparesMissing", 2),
          ("RebuildStarted", 3),
          ("RebuildFinished", 4),
          ("Fail", 5),
          ("FailSpare", 6),
          ("SpareActive", 7))
    )





class FmlHAEventId(Integer32):
    """Custom type FmlHAEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("MasterUnitSwitch", 1),
          ("SlaveUnitSwitch", 2),
          ("UnitShutdown", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fortinet_ObjectIdentity = ObjectIdentity
fortinet = _Fortinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356)
)
_Fortimail_ObjectIdentity = ObjectIdentity
fortimail = _Fortimail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1688)
)
_FmlTraps_ObjectIdentity = ObjectIdentity
fmlTraps = _FmlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 0)
)
_FmlSystem_ObjectIdentity = ObjectIdentity
fmlSystem = _FmlSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1)
)


class _FmlSysModel_Type(DisplayString):
    """Custom type fmlSysModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FmlSysModel_Type.__name__ = "DisplayString"
_FmlSysModel_Object = MibScalar
fmlSysModel = _FmlSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 1),
    _FmlSysModel_Type()
)
fmlSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysModel.setStatus("current")


class _FmlSysSerial_Type(DisplayString):
    """Custom type fmlSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmlSysSerial_Type.__name__ = "DisplayString"
_FmlSysSerial_Object = MibScalar
fmlSysSerial = _FmlSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 2),
    _FmlSysSerial_Type()
)
fmlSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysSerial.setStatus("current")


class _FmlSysVersion_Type(DisplayString):
    """Custom type fmlSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FmlSysVersion_Type.__name__ = "DisplayString"
_FmlSysVersion_Object = MibScalar
fmlSysVersion = _FmlSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 3),
    _FmlSysVersion_Type()
)
fmlSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysVersion.setStatus("current")


class _FmlSysVersionAv_Type(DisplayString):
    """Custom type fmlSysVersionAv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FmlSysVersionAv_Type.__name__ = "DisplayString"
_FmlSysVersionAv_Object = MibScalar
fmlSysVersionAv = _FmlSysVersionAv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 4),
    _FmlSysVersionAv_Type()
)
fmlSysVersionAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysVersionAv.setStatus("current")
_FmlSysOpMode_Type = FmlOpMode
_FmlSysOpMode_Object = MibScalar
fmlSysOpMode = _FmlSysOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 5),
    _FmlSysOpMode_Type()
)
fmlSysOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOpMode.setStatus("current")
_FmlSysCpuUsage_Type = Gauge32
_FmlSysCpuUsage_Object = MibScalar
fmlSysCpuUsage = _FmlSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 6),
    _FmlSysCpuUsage_Type()
)
fmlSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysCpuUsage.setStatus("current")
_FmlSysMemUsage_Type = Gauge32
_FmlSysMemUsage_Object = MibScalar
fmlSysMemUsage = _FmlSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 7),
    _FmlSysMemUsage_Type()
)
fmlSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysMemUsage.setStatus("current")
_FmlSysLogDiskUsage_Type = Gauge32
_FmlSysLogDiskUsage_Object = MibScalar
fmlSysLogDiskUsage = _FmlSysLogDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 8),
    _FmlSysLogDiskUsage_Type()
)
fmlSysLogDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysLogDiskUsage.setStatus("current")
_FmlSysMailDiskUsage_Type = Gauge32
_FmlSysMailDiskUsage_Object = MibScalar
fmlSysMailDiskUsage = _FmlSysMailDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 9),
    _FmlSysMailDiskUsage_Type()
)
fmlSysMailDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysMailDiskUsage.setStatus("current")
_FmlSysSesCount_Type = Gauge32
_FmlSysSesCount_Object = MibScalar
fmlSysSesCount = _FmlSysSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 10),
    _FmlSysSesCount_Type()
)
fmlSysSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysSesCount.setStatus("current")
_FmlSysEventCode_Type = FmlSysEventCode
_FmlSysEventCode_Object = MibScalar
fmlSysEventCode = _FmlSysEventCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 11),
    _FmlSysEventCode_Type()
)
fmlSysEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysEventCode.setStatus("current")
_FmlRAIDCode_Type = FmlRAIDCode
_FmlRAIDCode_Object = MibScalar
fmlRAIDCode = _FmlRAIDCode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 12),
    _FmlRAIDCode_Type()
)
fmlRAIDCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlRAIDCode.setStatus("current")


class _FmlRAIDDevName_Type(DisplayString):
    """Custom type fmlRAIDDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmlRAIDDevName_Type.__name__ = "DisplayString"
_FmlRAIDDevName_Object = MibScalar
fmlRAIDDevName = _FmlRAIDDevName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 13),
    _FmlRAIDDevName_Type()
)
fmlRAIDDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlRAIDDevName.setStatus("current")
_FmlHAEventId_Type = FmlHAEventId
_FmlHAEventId_Object = MibScalar
fmlHAEventId = _FmlHAEventId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 14),
    _FmlHAEventId_Type()
)
fmlHAEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHAEventId.setStatus("current")
_FmlHAUnitIp_Type = IpAddress
_FmlHAUnitIp_Object = MibScalar
fmlHAUnitIp = _FmlHAUnitIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 15),
    _FmlHAUnitIp_Type()
)
fmlHAUnitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHAUnitIp.setStatus("current")


class _FmlHAEventReason_Type(DisplayString):
    """Custom type fmlHAEventReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmlHAEventReason_Type.__name__ = "DisplayString"
_FmlHAEventReason_Object = MibScalar
fmlHAEventReason = _FmlHAEventReason_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 16),
    _FmlHAEventReason_Type()
)
fmlHAEventReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlHAEventReason.setStatus("current")
_FmlArchiveServerIp_Type = IpAddress
_FmlArchiveServerIp_Object = MibScalar
fmlArchiveServerIp = _FmlArchiveServerIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 18),
    _FmlArchiveServerIp_Type()
)
fmlArchiveServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlArchiveServerIp.setStatus("current")


class _FmlArchiveFilename_Type(DisplayString):
    """Custom type fmlArchiveFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmlArchiveFilename_Type.__name__ = "DisplayString"
_FmlArchiveFilename_Object = MibScalar
fmlArchiveFilename = _FmlArchiveFilename_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 19),
    _FmlArchiveFilename_Type()
)
fmlArchiveFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlArchiveFilename.setStatus("current")
_FmlSysOptions_ObjectIdentity = ObjectIdentity
fmlSysOptions = _FmlSysOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 101)
)
_FmlSysOptIdleTimeout_Type = Integer32
_FmlSysOptIdleTimeout_Object = MibScalar
fmlSysOptIdleTimeout = _FmlSysOptIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 101, 1),
    _FmlSysOptIdleTimeout_Type()
)
fmlSysOptIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOptIdleTimeout.setStatus("current")
_FmlSysOptAuthTimeout_Type = Integer32
_FmlSysOptAuthTimeout_Object = MibScalar
fmlSysOptAuthTimeout = _FmlSysOptAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 101, 2),
    _FmlSysOptAuthTimeout_Type()
)
fmlSysOptAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOptAuthTimeout.setStatus("current")
_FmlSysOptsLan_Type = FmlLanguageCode
_FmlSysOptsLan_Object = MibScalar
fmlSysOptsLan = _FmlSysOptsLan_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 101, 3),
    _FmlSysOptsLan_Type()
)
fmlSysOptsLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOptsLan.setStatus("current")
_FmlSysOptsLcdProt_Type = FmlBoolState
_FmlSysOptsLcdProt_Object = MibScalar
fmlSysOptsLcdProt = _FmlSysOptsLcdProt_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 101, 4),
    _FmlSysOptsLcdProt_Type()
)
fmlSysOptsLcdProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlSysOptsLcdProt.setStatus("current")
_FmlIp_ObjectIdentity = ObjectIdentity
fmlIp = _FmlIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102)
)
_FmlIpSessTable_Object = MibTable
fmlIpSessTable = _FmlIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2)
)
if mibBuilder.loadTexts:
    fmlIpSessTable.setStatus("current")
_FmlIpSessEntry_Object = MibTableRow
fmlIpSessEntry = _FmlIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1)
)
fmlIpSessEntry.setIndexNames(
    (0, "FORTIMAIL-MIB-220", "fmlIpSessIndex"),
)
if mibBuilder.loadTexts:
    fmlIpSessEntry.setStatus("current")
_FmlIpSessIndex_Type = FmlIndex
_FmlIpSessIndex_Object = MibTableColumn
fmlIpSessIndex = _FmlIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1, 1),
    _FmlIpSessIndex_Type()
)
fmlIpSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessIndex.setStatus("current")
_FmlIpSessProto_Type = FmlSessProto
_FmlIpSessProto_Object = MibTableColumn
fmlIpSessProto = _FmlIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1, 2),
    _FmlIpSessProto_Type()
)
fmlIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessProto.setStatus("current")
_FmlIpSessFromAddr_Type = IpAddress
_FmlIpSessFromAddr_Object = MibTableColumn
fmlIpSessFromAddr = _FmlIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1, 3),
    _FmlIpSessFromAddr_Type()
)
fmlIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessFromAddr.setStatus("current")


class _FmlIpSessFromPort_Type(Integer32):
    """Custom type fmlIpSessFromPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FmlIpSessFromPort_Type.__name__ = "Integer32"
_FmlIpSessFromPort_Object = MibTableColumn
fmlIpSessFromPort = _FmlIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1, 4),
    _FmlIpSessFromPort_Type()
)
fmlIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessFromPort.setStatus("current")
_FmlIpSessToAddr_Type = IpAddress
_FmlIpSessToAddr_Object = MibTableColumn
fmlIpSessToAddr = _FmlIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1, 5),
    _FmlIpSessToAddr_Type()
)
fmlIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessToAddr.setStatus("current")


class _FmlIpSessToPort_Type(Integer32):
    """Custom type fmlIpSessToPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FmlIpSessToPort_Type.__name__ = "Integer32"
_FmlIpSessToPort_Object = MibTableColumn
fmlIpSessToPort = _FmlIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1, 6),
    _FmlIpSessToPort_Type()
)
fmlIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessToPort.setStatus("current")
_FmlIpSessExp_Type = Counter32
_FmlIpSessExp_Object = MibTableColumn
fmlIpSessExp = _FmlIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 102, 2, 1, 7),
    _FmlIpSessExp_Type()
)
fmlIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlIpSessExp.setStatus("current")
_FmlMailOptions_ObjectIdentity = ObjectIdentity
fmlMailOptions = _FmlMailOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 103)
)
_FmlMailOptionsDeferQueue_Type = Counter32
_FmlMailOptionsDeferQueue_Object = MibScalar
fmlMailOptionsDeferQueue = _FmlMailOptionsDeferQueue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1688, 1, 103, 1),
    _FmlMailOptionsDeferQueue_Type()
)
fmlMailOptionsDeferQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmlMailOptionsDeferQueue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTIMAIL-MIB-220",
    **{"FmlBoolState": FmlBoolState,
       "FmlIndex": FmlIndex,
       "FmlOpMode": FmlOpMode,
       "FmlSessProto": FmlSessProto,
       "FmlLanguageCode": FmlLanguageCode,
       "FmlSysEventCode": FmlSysEventCode,
       "FmlRAIDCode": FmlRAIDCode,
       "FmlHAEventId": FmlHAEventId,
       "fortinet": fortinet,
       "fortimail": fortimail,
       "fmlTraps": fmlTraps,
       "fmlSystem": fmlSystem,
       "fmlSysModel": fmlSysModel,
       "fmlSysSerial": fmlSysSerial,
       "fmlSysVersion": fmlSysVersion,
       "fmlSysVersionAv": fmlSysVersionAv,
       "fmlSysOpMode": fmlSysOpMode,
       "fmlSysCpuUsage": fmlSysCpuUsage,
       "fmlSysMemUsage": fmlSysMemUsage,
       "fmlSysLogDiskUsage": fmlSysLogDiskUsage,
       "fmlSysMailDiskUsage": fmlSysMailDiskUsage,
       "fmlSysSesCount": fmlSysSesCount,
       "fmlSysEventCode": fmlSysEventCode,
       "fmlRAIDCode": fmlRAIDCode,
       "fmlRAIDDevName": fmlRAIDDevName,
       "fmlHAEventId": fmlHAEventId,
       "fmlHAUnitIp": fmlHAUnitIp,
       "fmlHAEventReason": fmlHAEventReason,
       "fmlArchiveServerIp": fmlArchiveServerIp,
       "fmlArchiveFilename": fmlArchiveFilename,
       "fmlSysOptions": fmlSysOptions,
       "fmlSysOptIdleTimeout": fmlSysOptIdleTimeout,
       "fmlSysOptAuthTimeout": fmlSysOptAuthTimeout,
       "fmlSysOptsLan": fmlSysOptsLan,
       "fmlSysOptsLcdProt": fmlSysOptsLcdProt,
       "fmlIp": fmlIp,
       "fmlIpSessTable": fmlIpSessTable,
       "fmlIpSessEntry": fmlIpSessEntry,
       "fmlIpSessIndex": fmlIpSessIndex,
       "fmlIpSessProto": fmlIpSessProto,
       "fmlIpSessFromAddr": fmlIpSessFromAddr,
       "fmlIpSessFromPort": fmlIpSessFromPort,
       "fmlIpSessToAddr": fmlIpSessToAddr,
       "fmlIpSessToPort": fmlIpSessToPort,
       "fmlIpSessExp": fmlIpSessExp,
       "fmlMailOptions": fmlMailOptions,
       "fmlMailOptionsDeferQueue": fmlMailOptionsDeferQueue}
)

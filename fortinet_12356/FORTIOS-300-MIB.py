# SNMP MIB module (FORTIOS-300-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/fortinet_12356/FORTIOS-300-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:36:32 2025
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

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex")

(InetPortNumber,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

fortinet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356)
)
if mibBuilder.loadTexts:
    fortinet.setRevisions(
        ("2008-06-19 00:00",
         "2008-06-16 00:00",
         "2008-04-14 00:00",
         "2008-04-09 00:00",
         "2008-01-10 00:00",
         "2008-01-02 00:00",
         "2007-12-05 00:00",
         "2007-11-27 00:00",
         "2007-11-05 00:00",
         "2007-09-12 00:00",
         "2007-08-09 00:00",
         "2007-06-06 00:00",
         "2006-11-23 00:00",
         "2006-08-03 00:00",
         "2006-07-31 00:00",
         "2006-07-28 00:00",
         "2006-06-21 00:00",
         "2006-04-26 00:00",
         "2006-01-09 00:00",
         "2005-12-07 00:00",
         "2005-09-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FnBoolState(TextualConvention, Integer32):
    status = "current"
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



class FnIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class FnVdIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FnOpMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nat", 1),
          ("transparent", 2))
    )



class FnHaMode(TextualConvention, Integer32):
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
        *(("standalone", 1),
          ("activeActive", 2),
          ("activePassive", 3))
    )



class FnHaLBSchedule(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("hub", 2),
          ("leastConnections", 3),
          ("roundRobin", 4),
          ("weightedRoundRobin", 5),
          ("random", 6),
          ("ipBased", 7),
          ("ipPortBased", 8))
    )



class FnAdminPermLevel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("readAdmin", 0),
          ("writeAdmin", 1),
          ("domainAdmin", 15),
          ("superAdmin", 255))
    )



class FnUserAuthType(TextualConvention, Integer32):
    status = "current"
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
          ("radiusSingle", 2),
          ("radiusMultiple", 3),
          ("ldap", 4))
    )



class FnLanguage(TextualConvention, Integer32):
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("english", 1),
          ("simplifiedChinese", 2),
          ("japanese", 3),
          ("korean", 4),
          ("spanish", 5),
          ("traditionalChinese", 6),
          ("french", 7),
          ("undefined", 255))
    )



class FnSessProto(TextualConvention, Integer32):
    status = "current"
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



class FnModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              302,
              500,
              501,
              502,
              510,
              600,
              601,
              602,
              603,
              610,
              611,
              612,
              613,
              1000,
              1001,
              2000,
              2001,
              3000,
              3001,
              3002,
              4000,
              4001,
              5000,
              5001,
              8000,
              8001,
              10000,
              10001,
              10002,
              10003,
              20000,
              30000,
              30160,
              36000,
              36003,
              38100,
              40000,
              50000,
              50001,
              50011,
              50021,
              50040,
              50050,
              50051)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("fgt30B", 302),
          ("fgt50A", 500),
          ("fgt50AM", 501),
          ("fgt50B", 502),
          ("fwf50B", 510),
          ("fgt60", 600),
          ("fgt60M", 601),
          ("fgt60ADSL", 602),
          ("fgt60B", 603),
          ("fwf60", 610),
          ("fwf60A", 611),
          ("fwf60AM", 612),
          ("fwf60B", 613),
          ("fgt100", 1000),
          ("fgt100A", 1001),
          ("fgt200", 2000),
          ("fgt200A", 2001),
          ("fgt300", 3000),
          ("fgt300A", 3001),
          ("fgt310B", 3002),
          ("fgt400", 4000),
          ("fgt400A", 4001),
          ("fgt500", 5000),
          ("fgt500A", 5001),
          ("fgt800", 8000),
          ("fgt800F", 8001),
          ("fgt1000", 10000),
          ("fgt1000A", 10001),
          ("fgt1000AFA2", 10002),
          ("fgt1000ALENC", 10003),
          ("fgt2000", 20000),
          ("fgt3000", 30000),
          ("fgt3016B", 30160),
          ("fgt3600", 36000),
          ("fgt3600A", 36003),
          ("fgt3810A", 38100),
          ("fgt4000", 40000),
          ("fgt5000", 50000),
          ("fgt5002FB2", 50001),
          ("fgt5001A", 50011),
          ("fgt5002A", 50021),
          ("fgt5004", 50040),
          ("fgt5005", 50050),
          ("fgt5005FA2", 50051))
    )



class FnP2PProto(TextualConvention, Integer32):
    status = "current"
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
        *(("bitTorrent", 0),
          ("eDonkey", 1),
          ("gnutella", 2),
          ("kaZaa", 3),
          ("skype", 4),
          ("winNY", 5))
    )



# MIB Managed Objects in the order of their OIDs

_FnTraps_ObjectIdentity = ObjectIdentity
fnTraps = _FnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 0)
)
_FnTrapObjects_ObjectIdentity = ObjectIdentity
fnTrapObjects = _FnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 0, 1)
)
_FnGenTrapMsg_Type = DisplayString
_FnGenTrapMsg_Object = MibScalar
fnGenTrapMsg = _FnGenTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 0, 1, 1),
    _FnGenTrapMsg_Type()
)
fnGenTrapMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnGenTrapMsg.setStatus("current")
_FnSystem_ObjectIdentity = ObjectIdentity
fnSystem = _FnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1)
)
_FnSysModel_Type = FnModel
_FnSysModel_Object = MibScalar
fnSysModel = _FnSysModel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 1),
    _FnSysModel_Type()
)
fnSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysModel.setStatus("current")


class _FnSysSerial_Type(DisplayString):
    """Custom type fnSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnSysSerial_Type.__name__ = "DisplayString"
_FnSysSerial_Object = MibScalar
fnSysSerial = _FnSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 2),
    _FnSysSerial_Type()
)
fnSysSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSerial.setStatus("current")


class _FnSysVersion_Type(DisplayString):
    """Custom type fnSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysVersion_Type.__name__ = "DisplayString"
_FnSysVersion_Object = MibScalar
fnSysVersion = _FnSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 3),
    _FnSysVersion_Type()
)
fnSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysVersion.setStatus("current")


class _FnSysVersionAv_Type(DisplayString):
    """Custom type fnSysVersionAv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysVersionAv_Type.__name__ = "DisplayString"
_FnSysVersionAv_Object = MibScalar
fnSysVersionAv = _FnSysVersionAv_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 4),
    _FnSysVersionAv_Type()
)
fnSysVersionAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysVersionAv.setStatus("current")


class _FnSysVersionNids_Type(DisplayString):
    """Custom type fnSysVersionNids based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FnSysVersionNids_Type.__name__ = "DisplayString"
_FnSysVersionNids_Object = MibScalar
fnSysVersionNids = _FnSysVersionNids_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 5),
    _FnSysVersionNids_Type()
)
fnSysVersionNids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysVersionNids.setStatus("current")
_FnSysHaMode_Type = FnHaMode
_FnSysHaMode_Object = MibScalar
fnSysHaMode = _FnSysHaMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 6),
    _FnSysHaMode_Type()
)
fnSysHaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysHaMode.setStatus("current")
_FnSysOpMode_Type = FnOpMode
_FnSysOpMode_Object = MibScalar
fnSysOpMode = _FnSysOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 7),
    _FnSysOpMode_Type()
)
fnSysOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysOpMode.setStatus("current")


class _FnSysCpuUsage_Type(Gauge32):
    """Custom type fnSysCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnSysCpuUsage_Type.__name__ = "Gauge32"
_FnSysCpuUsage_Object = MibScalar
fnSysCpuUsage = _FnSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 8),
    _FnSysCpuUsage_Type()
)
fnSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysCpuUsage.setStatus("current")


class _FnSysMemUsage_Type(Gauge32):
    """Custom type fnSysMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnSysMemUsage_Type.__name__ = "Gauge32"
_FnSysMemUsage_Object = MibScalar
fnSysMemUsage = _FnSysMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 9),
    _FnSysMemUsage_Type()
)
fnSysMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMemUsage.setStatus("current")
_FnSysSesCount_Type = Gauge32
_FnSysSesCount_Object = MibScalar
fnSysSesCount = _FnSysSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 10),
    _FnSysSesCount_Type()
)
fnSysSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysSesCount.setStatus("current")
_FnSysDiskCapacity_Type = Gauge32
_FnSysDiskCapacity_Object = MibScalar
fnSysDiskCapacity = _FnSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 11),
    _FnSysDiskCapacity_Type()
)
fnSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysDiskCapacity.setStatus("current")
_FnSysDiskUsage_Type = Gauge32
_FnSysDiskUsage_Object = MibScalar
fnSysDiskUsage = _FnSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 12),
    _FnSysDiskUsage_Type()
)
fnSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysDiskUsage.setStatus("current")
_FnSysMemCapacity_Type = Gauge32
_FnSysMemCapacity_Object = MibScalar
fnSysMemCapacity = _FnSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 13),
    _FnSysMemCapacity_Type()
)
fnSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnSysMemCapacity.setStatus("current")
_FnHa_ObjectIdentity = ObjectIdentity
fnHa = _FnHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100)
)
_FnHaGroupId_Type = FnIndex
_FnHaGroupId_Object = MibScalar
fnHaGroupId = _FnHaGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 1),
    _FnHaGroupId_Type()
)
fnHaGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaGroupId.setStatus("current")


class _FnHaPriority_Type(Integer32):
    """Custom type fnHaPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FnHaPriority_Type.__name__ = "Integer32"
_FnHaPriority_Object = MibScalar
fnHaPriority = _FnHaPriority_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 2),
    _FnHaPriority_Type()
)
fnHaPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaPriority.setStatus("current")
_FnHaOverride_Type = FnBoolState
_FnHaOverride_Object = MibScalar
fnHaOverride = _FnHaOverride_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 3),
    _FnHaOverride_Type()
)
fnHaOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaOverride.setStatus("current")
_FnHaAutoSync_Type = FnBoolState
_FnHaAutoSync_Object = MibScalar
fnHaAutoSync = _FnHaAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 4),
    _FnHaAutoSync_Type()
)
fnHaAutoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaAutoSync.setStatus("current")
_FnHaSchedule_Type = FnHaLBSchedule
_FnHaSchedule_Object = MibScalar
fnHaSchedule = _FnHaSchedule_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 5),
    _FnHaSchedule_Type()
)
fnHaSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaSchedule.setStatus("current")
_FnHaStatsTable_Object = MibTable
fnHaStatsTable = _FnHaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6)
)
if mibBuilder.loadTexts:
    fnHaStatsTable.setStatus("current")
_FnHaStatsEntry_Object = MibTableRow
fnHaStatsEntry = _FnHaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1)
)
fnHaStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnHaStatsIndex"),
)
if mibBuilder.loadTexts:
    fnHaStatsEntry.setStatus("current")
_FnHaStatsIndex_Type = FnIndex
_FnHaStatsIndex_Object = MibTableColumn
fnHaStatsIndex = _FnHaStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 1),
    _FnHaStatsIndex_Type()
)
fnHaStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnHaStatsIndex.setStatus("current")


class _FnHaStatsSerial_Type(DisplayString):
    """Custom type fnHaStatsSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnHaStatsSerial_Type.__name__ = "DisplayString"
_FnHaStatsSerial_Object = MibTableColumn
fnHaStatsSerial = _FnHaStatsSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 2),
    _FnHaStatsSerial_Type()
)
fnHaStatsSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsSerial.setStatus("current")


class _FnHaStatsCpuUsage_Type(Gauge32):
    """Custom type fnHaStatsCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnHaStatsCpuUsage_Type.__name__ = "Gauge32"
_FnHaStatsCpuUsage_Object = MibTableColumn
fnHaStatsCpuUsage = _FnHaStatsCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 3),
    _FnHaStatsCpuUsage_Type()
)
fnHaStatsCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsCpuUsage.setStatus("current")


class _FnHaStatsMemUsage_Type(Gauge32):
    """Custom type fnHaStatsMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnHaStatsMemUsage_Type.__name__ = "Gauge32"
_FnHaStatsMemUsage_Object = MibTableColumn
fnHaStatsMemUsage = _FnHaStatsMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 4),
    _FnHaStatsMemUsage_Type()
)
fnHaStatsMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsMemUsage.setStatus("current")
_FnHaStatsNetUsage_Type = Gauge32
_FnHaStatsNetUsage_Object = MibTableColumn
fnHaStatsNetUsage = _FnHaStatsNetUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 5),
    _FnHaStatsNetUsage_Type()
)
fnHaStatsNetUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsNetUsage.setStatus("current")
_FnHaStatsSesCount_Type = Gauge32
_FnHaStatsSesCount_Object = MibTableColumn
fnHaStatsSesCount = _FnHaStatsSesCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 6),
    _FnHaStatsSesCount_Type()
)
fnHaStatsSesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsSesCount.setStatus("current")
_FnHaStatsPktCount_Type = Counter32
_FnHaStatsPktCount_Object = MibTableColumn
fnHaStatsPktCount = _FnHaStatsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 7),
    _FnHaStatsPktCount_Type()
)
fnHaStatsPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsPktCount.setStatus("current")
_FnHaStatsByteCount_Type = Counter32
_FnHaStatsByteCount_Object = MibTableColumn
fnHaStatsByteCount = _FnHaStatsByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 8),
    _FnHaStatsByteCount_Type()
)
fnHaStatsByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsByteCount.setStatus("current")
_FnHaStatsIdsCount_Type = Counter32
_FnHaStatsIdsCount_Object = MibTableColumn
fnHaStatsIdsCount = _FnHaStatsIdsCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 9),
    _FnHaStatsIdsCount_Type()
)
fnHaStatsIdsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsIdsCount.setStatus("current")
_FnHaStatsAvCount_Type = Counter32
_FnHaStatsAvCount_Object = MibTableColumn
fnHaStatsAvCount = _FnHaStatsAvCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 10),
    _FnHaStatsAvCount_Type()
)
fnHaStatsAvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsAvCount.setStatus("current")


class _FnHaStatsHostname_Type(DisplayString):
    """Custom type fnHaStatsHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FnHaStatsHostname_Type.__name__ = "DisplayString"
_FnHaStatsHostname_Object = MibTableColumn
fnHaStatsHostname = _FnHaStatsHostname_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 6, 1, 11),
    _FnHaStatsHostname_Type()
)
fnHaStatsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaStatsHostname.setStatus("current")
_FnHaGroupName_Type = DisplayString
_FnHaGroupName_Object = MibScalar
fnHaGroupName = _FnHaGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 7),
    _FnHaGroupName_Type()
)
fnHaGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHaGroupName.setStatus("current")
_FnHaTrapMemberSerial_Type = DisplayString
_FnHaTrapMemberSerial_Object = MibScalar
fnHaTrapMemberSerial = _FnHaTrapMemberSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 100, 8),
    _FnHaTrapMemberSerial_Type()
)
fnHaTrapMemberSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnHaTrapMemberSerial.setStatus("current")
_FnAdmin_ObjectIdentity = ObjectIdentity
fnAdmin = _FnAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101)
)
_FnAdminNumber_Type = Integer32
_FnAdminNumber_Object = MibScalar
fnAdminNumber = _FnAdminNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 1),
    _FnAdminNumber_Type()
)
fnAdminNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminNumber.setStatus("current")
_FnAdminTable_Object = MibTable
fnAdminTable = _FnAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2)
)
if mibBuilder.loadTexts:
    fnAdminTable.setStatus("current")
_FnAdminEntry_Object = MibTableRow
fnAdminEntry = _FnAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1)
)
fnAdminEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnAdminIndex"),
)
if mibBuilder.loadTexts:
    fnAdminEntry.setStatus("current")
_FnAdminIndex_Type = FnIndex
_FnAdminIndex_Object = MibTableColumn
fnAdminIndex = _FnAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 1),
    _FnAdminIndex_Type()
)
fnAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAdminIndex.setStatus("current")
_FnAdminName_Type = DisplayString
_FnAdminName_Object = MibTableColumn
fnAdminName = _FnAdminName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 2),
    _FnAdminName_Type()
)
fnAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminName.setStatus("current")
_FnAdminAddr_Type = IpAddress
_FnAdminAddr_Object = MibTableColumn
fnAdminAddr = _FnAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 3),
    _FnAdminAddr_Type()
)
fnAdminAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminAddr.setStatus("current")
_FnAdminMask_Type = IpAddress
_FnAdminMask_Object = MibTableColumn
fnAdminMask = _FnAdminMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 4),
    _FnAdminMask_Type()
)
fnAdminMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminMask.setStatus("current")
_FnAdminVdom_Type = FnVdIndex
_FnAdminVdom_Object = MibTableColumn
fnAdminVdom = _FnAdminVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 101, 2, 1, 5),
    _FnAdminVdom_Type()
)
fnAdminVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAdminVdom.setStatus("current")
_FnUsers_ObjectIdentity = ObjectIdentity
fnUsers = _FnUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102)
)
_FnUserNumber_Type = Integer32
_FnUserNumber_Object = MibScalar
fnUserNumber = _FnUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 1),
    _FnUserNumber_Type()
)
fnUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserNumber.setStatus("current")
_FnUserTable_Object = MibTable
fnUserTable = _FnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2)
)
if mibBuilder.loadTexts:
    fnUserTable.setStatus("current")
_FnUserEntry_Object = MibTableRow
fnUserEntry = _FnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1)
)
fnUserEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnUserIndex"),
)
if mibBuilder.loadTexts:
    fnUserEntry.setStatus("current")
_FnUserIndex_Type = FnIndex
_FnUserIndex_Object = MibTableColumn
fnUserIndex = _FnUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 1),
    _FnUserIndex_Type()
)
fnUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnUserIndex.setStatus("current")
_FnUserName_Type = DisplayString
_FnUserName_Object = MibTableColumn
fnUserName = _FnUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 2),
    _FnUserName_Type()
)
fnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserName.setStatus("current")
_FnUserAuth_Type = FnUserAuthType
_FnUserAuth_Object = MibTableColumn
fnUserAuth = _FnUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 3),
    _FnUserAuth_Type()
)
fnUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserAuth.setStatus("current")
_FnUserState_Type = FnBoolState
_FnUserState_Object = MibTableColumn
fnUserState = _FnUserState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 4),
    _FnUserState_Type()
)
fnUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserState.setStatus("current")
_FnUserVdom_Type = FnVdIndex
_FnUserVdom_Object = MibTableColumn
fnUserVdom = _FnUserVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 102, 2, 1, 5),
    _FnUserVdom_Type()
)
fnUserVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnUserVdom.setStatus("current")
_FnOptions_ObjectIdentity = ObjectIdentity
fnOptions = _FnOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 103)
)
_FnOptIdleTimeout_Type = Integer32
_FnOptIdleTimeout_Object = MibScalar
fnOptIdleTimeout = _FnOptIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 103, 1),
    _FnOptIdleTimeout_Type()
)
fnOptIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOptIdleTimeout.setStatus("current")
_FnOptAuthTimeout_Type = Integer32
_FnOptAuthTimeout_Object = MibScalar
fnOptAuthTimeout = _FnOptAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 103, 2),
    _FnOptAuthTimeout_Type()
)
fnOptAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOptAuthTimeout.setStatus("current")
_FnOptLanguage_Type = FnLanguage
_FnOptLanguage_Object = MibScalar
fnOptLanguage = _FnOptLanguage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 103, 3),
    _FnOptLanguage_Type()
)
fnOptLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOptLanguage.setStatus("current")
_FnOptLcdProtection_Type = FnBoolState
_FnOptLcdProtection_Object = MibScalar
fnOptLcdProtection = _FnOptLcdProtection_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 103, 4),
    _FnOptLcdProtection_Type()
)
fnOptLcdProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOptLcdProtection.setStatus("current")
_FnHwSensors_ObjectIdentity = ObjectIdentity
fnHwSensors = _FnHwSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110)
)
_FnHwSensorCount_Type = Integer32
_FnHwSensorCount_Object = MibScalar
fnHwSensorCount = _FnHwSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110, 1),
    _FnHwSensorCount_Type()
)
fnHwSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHwSensorCount.setStatus("current")
_FnHwSensorTable_Object = MibTable
fnHwSensorTable = _FnHwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110, 2)
)
if mibBuilder.loadTexts:
    fnHwSensorTable.setStatus("current")
_FnHwSensorEntry_Object = MibTableRow
fnHwSensorEntry = _FnHwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110, 2, 1)
)
fnHwSensorEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnHwSensorEntIndex"),
)
if mibBuilder.loadTexts:
    fnHwSensorEntry.setStatus("current")
_FnHwSensorEntIndex_Type = FnIndex
_FnHwSensorEntIndex_Object = MibTableColumn
fnHwSensorEntIndex = _FnHwSensorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110, 2, 1, 1),
    _FnHwSensorEntIndex_Type()
)
fnHwSensorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnHwSensorEntIndex.setStatus("current")
_FnHwSensorEntName_Type = DisplayString
_FnHwSensorEntName_Object = MibTableColumn
fnHwSensorEntName = _FnHwSensorEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110, 2, 1, 2),
    _FnHwSensorEntName_Type()
)
fnHwSensorEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHwSensorEntName.setStatus("current")
_FnHwSensorEntValue_Type = DisplayString
_FnHwSensorEntValue_Object = MibTableColumn
fnHwSensorEntValue = _FnHwSensorEntValue_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110, 2, 1, 3),
    _FnHwSensorEntValue_Type()
)
fnHwSensorEntValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHwSensorEntValue.setStatus("current")


class _FnHwSensorEntAlarmStatus_Type(Integer32):
    """Custom type fnHwSensorEntAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FnHwSensorEntAlarmStatus_Type.__name__ = "Integer32"
_FnHwSensorEntAlarmStatus_Object = MibTableColumn
fnHwSensorEntAlarmStatus = _FnHwSensorEntAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 1, 110, 2, 1, 4),
    _FnHwSensorEntAlarmStatus_Type()
)
fnHwSensorEntAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnHwSensorEntAlarmStatus.setStatus("current")
_FnDomains_ObjectIdentity = ObjectIdentity
fnDomains = _FnDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 2)
)
_FnVdNumber_Type = Integer32
_FnVdNumber_Object = MibScalar
fnVdNumber = _FnVdNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 1),
    _FnVdNumber_Type()
)
fnVdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdNumber.setStatus("current")
_FnVdTable_Object = MibTable
fnVdTable = _FnVdTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2)
)
if mibBuilder.loadTexts:
    fnVdTable.setStatus("current")
_FnVdEntry_Object = MibTableRow
fnVdEntry = _FnVdEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1)
)
fnVdEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnVdEntIndex"),
)
if mibBuilder.loadTexts:
    fnVdEntry.setStatus("current")
_FnVdEntIndex_Type = FnVdIndex
_FnVdEntIndex_Object = MibTableColumn
fnVdEntIndex = _FnVdEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 1),
    _FnVdEntIndex_Type()
)
fnVdEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVdEntIndex.setStatus("current")
_FnVdEntName_Type = DisplayString
_FnVdEntName_Object = MibTableColumn
fnVdEntName = _FnVdEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 2),
    _FnVdEntName_Type()
)
fnVdEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdEntName.setStatus("current")
_FnVdEntOpMode_Type = FnOpMode
_FnVdEntOpMode_Object = MibTableColumn
fnVdEntOpMode = _FnVdEntOpMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 2, 1, 3),
    _FnVdEntOpMode_Type()
)
fnVdEntOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdEntOpMode.setStatus("current")
_FnVdMaxVdoms_Type = Integer32
_FnVdMaxVdoms_Object = MibScalar
fnVdMaxVdoms = _FnVdMaxVdoms_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 3),
    _FnVdMaxVdoms_Type()
)
fnVdMaxVdoms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdMaxVdoms.setStatus("current")
_FnVdEnabled_Type = FnBoolState
_FnVdEnabled_Object = MibScalar
fnVdEnabled = _FnVdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 2, 4),
    _FnVdEnabled_Type()
)
fnVdEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVdEnabled.setStatus("current")
_FnIntf_ObjectIdentity = ObjectIdentity
fnIntf = _FnIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 3)
)
_FnIntfTable_Object = MibTable
fnIntfTable = _FnIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1)
)
if mibBuilder.loadTexts:
    fnIntfTable.setStatus("current")
_FnIntfEntry_Object = MibTableRow
fnIntfEntry = _FnIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fnIntfEntry.setStatus("current")
_FnIntfEntVdom_Type = FnVdIndex
_FnIntfEntVdom_Object = MibTableColumn
fnIntfEntVdom = _FnIntfEntVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 3, 1, 1, 1),
    _FnIntfEntVdom_Type()
)
fnIntfEntVdom.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnIntfEntVdom.setStatus("current")
_FnIp_ObjectIdentity = ObjectIdentity
fnIp = _FnIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 4)
)
_FnIpSessTable_Object = MibTable
fnIpSessTable = _FnIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2)
)
if mibBuilder.loadTexts:
    fnIpSessTable.setStatus("current")
_FnIpSessEntry_Object = MibTableRow
fnIpSessEntry = _FnIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1)
)
fnIpSessEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnIpSessIndex"),
)
if mibBuilder.loadTexts:
    fnIpSessEntry.setStatus("current")
_FnIpSessIndex_Type = FnIndex
_FnIpSessIndex_Object = MibTableColumn
fnIpSessIndex = _FnIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 1),
    _FnIpSessIndex_Type()
)
fnIpSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnIpSessIndex.setStatus("current")
_FnIpSessProto_Type = FnSessProto
_FnIpSessProto_Object = MibTableColumn
fnIpSessProto = _FnIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 2),
    _FnIpSessProto_Type()
)
fnIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessProto.setStatus("current")
_FnIpSessFromAddr_Type = IpAddress
_FnIpSessFromAddr_Object = MibTableColumn
fnIpSessFromAddr = _FnIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 3),
    _FnIpSessFromAddr_Type()
)
fnIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessFromAddr.setStatus("current")
_FnIpSessFromPort_Type = InetPortNumber
_FnIpSessFromPort_Object = MibTableColumn
fnIpSessFromPort = _FnIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 4),
    _FnIpSessFromPort_Type()
)
fnIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessFromPort.setStatus("current")
_FnIpSessToAddr_Type = IpAddress
_FnIpSessToAddr_Object = MibTableColumn
fnIpSessToAddr = _FnIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 5),
    _FnIpSessToAddr_Type()
)
fnIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessToAddr.setStatus("current")
_FnIpSessToPort_Type = InetPortNumber
_FnIpSessToPort_Object = MibTableColumn
fnIpSessToPort = _FnIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 6),
    _FnIpSessToPort_Type()
)
fnIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessToPort.setStatus("current")
_FnIpSessExp_Type = Counter32
_FnIpSessExp_Object = MibTableColumn
fnIpSessExp = _FnIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 7),
    _FnIpSessExp_Type()
)
fnIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessExp.setStatus("current")
_FnIpSessVdom_Type = FnVdIndex
_FnIpSessVdom_Object = MibTableColumn
fnIpSessVdom = _FnIpSessVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 2, 1, 8),
    _FnIpSessVdom_Type()
)
fnIpSessVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessVdom.setStatus("current")
_FnIpSessStatsTable_Object = MibTable
fnIpSessStatsTable = _FnIpSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3)
)
if mibBuilder.loadTexts:
    fnIpSessStatsTable.setStatus("current")
_FnIpSessStatsEntry_Object = MibTableRow
fnIpSessStatsEntry = _FnIpSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3, 1)
)
fnIpSessStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnIpSessStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnIpSessStatsEntry.setStatus("current")
_FnIpSessStatsVdomIndex_Type = FnVdIndex
_FnIpSessStatsVdomIndex_Object = MibTableColumn
fnIpSessStatsVdomIndex = _FnIpSessStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3, 1, 1),
    _FnIpSessStatsVdomIndex_Type()
)
fnIpSessStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnIpSessStatsVdomIndex.setStatus("current")
_FnIpSessNumber_Type = Counter32
_FnIpSessNumber_Object = MibTableColumn
fnIpSessNumber = _FnIpSessNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 4, 3, 1, 2),
    _FnIpSessNumber_Type()
)
fnIpSessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpSessNumber.setStatus("current")
_FnFirewall_ObjectIdentity = ObjectIdentity
fnFirewall = _FnFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 8)
)
_FnFwPolicyStatsTable_Object = MibTable
fnFwPolicyStatsTable = _FnFwPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1)
)
if mibBuilder.loadTexts:
    fnFwPolicyStatsTable.setStatus("current")
_FnFwPolicyStatsEntry_Object = MibTableRow
fnFwPolicyStatsEntry = _FnFwPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1)
)
fnFwPolicyStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnFwPolicyStatsVdomIndex"),
    (0, "FORTIOS-300-MIB", "fnFwPolicyID"),
)
if mibBuilder.loadTexts:
    fnFwPolicyStatsEntry.setStatus("current")
_FnFwPolicyStatsVdomIndex_Type = FnVdIndex
_FnFwPolicyStatsVdomIndex_Object = MibTableColumn
fnFwPolicyStatsVdomIndex = _FnFwPolicyStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 1),
    _FnFwPolicyStatsVdomIndex_Type()
)
fnFwPolicyStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnFwPolicyStatsVdomIndex.setStatus("current")
_FnFwPolicyID_Type = FnIndex
_FnFwPolicyID_Object = MibTableColumn
fnFwPolicyID = _FnFwPolicyID_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 2),
    _FnFwPolicyID_Type()
)
fnFwPolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnFwPolicyID.setStatus("current")
_FnFwPolicyPktCount_Type = Counter32
_FnFwPolicyPktCount_Object = MibTableColumn
fnFwPolicyPktCount = _FnFwPolicyPktCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 3),
    _FnFwPolicyPktCount_Type()
)
fnFwPolicyPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwPolicyPktCount.setStatus("current")
_FnFwPolicyByteCount_Type = Counter32
_FnFwPolicyByteCount_Object = MibTableColumn
fnFwPolicyByteCount = _FnFwPolicyByteCount_Object(
    (1, 3, 6, 1, 4, 1, 12356, 8, 1, 1, 4),
    _FnFwPolicyByteCount_Type()
)
fnFwPolicyByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFwPolicyByteCount.setStatus("current")
_FnVpn_ObjectIdentity = ObjectIdentity
fnVpn = _FnVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 9)
)
_FnVpnDialupTable_Object = MibTable
fnVpnDialupTable = _FnVpnDialupTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1)
)
if mibBuilder.loadTexts:
    fnVpnDialupTable.setStatus("current")
_FnVpnDialupEntry_Object = MibTableRow
fnVpnDialupEntry = _FnVpnDialupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1)
)
fnVpnDialupEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnVpnDialupIndex"),
)
if mibBuilder.loadTexts:
    fnVpnDialupEntry.setStatus("current")
_FnVpnDialupIndex_Type = FnIndex
_FnVpnDialupIndex_Object = MibTableColumn
fnVpnDialupIndex = _FnVpnDialupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 1),
    _FnVpnDialupIndex_Type()
)
fnVpnDialupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnDialupIndex.setStatus("current")
_FnVpnDialupGateway_Type = IpAddress
_FnVpnDialupGateway_Object = MibTableColumn
fnVpnDialupGateway = _FnVpnDialupGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 2),
    _FnVpnDialupGateway_Type()
)
fnVpnDialupGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupGateway.setStatus("current")
_FnVpnDialupLifetime_Type = Integer32
_FnVpnDialupLifetime_Object = MibTableColumn
fnVpnDialupLifetime = _FnVpnDialupLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 3),
    _FnVpnDialupLifetime_Type()
)
fnVpnDialupLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupLifetime.setStatus("current")
_FnVpnDialupTimeout_Type = Integer32
_FnVpnDialupTimeout_Object = MibTableColumn
fnVpnDialupTimeout = _FnVpnDialupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 4),
    _FnVpnDialupTimeout_Type()
)
fnVpnDialupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupTimeout.setStatus("current")
_FnVpnDialupSrcBegin_Type = IpAddress
_FnVpnDialupSrcBegin_Object = MibTableColumn
fnVpnDialupSrcBegin = _FnVpnDialupSrcBegin_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 5),
    _FnVpnDialupSrcBegin_Type()
)
fnVpnDialupSrcBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupSrcBegin.setStatus("current")
_FnVpnDialupSrcEnd_Type = IpAddress
_FnVpnDialupSrcEnd_Object = MibTableColumn
fnVpnDialupSrcEnd = _FnVpnDialupSrcEnd_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 6),
    _FnVpnDialupSrcEnd_Type()
)
fnVpnDialupSrcEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupSrcEnd.setStatus("current")
_FnVpnDialupDstAddr_Type = IpAddress
_FnVpnDialupDstAddr_Object = MibTableColumn
fnVpnDialupDstAddr = _FnVpnDialupDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 7),
    _FnVpnDialupDstAddr_Type()
)
fnVpnDialupDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupDstAddr.setStatus("current")
_FnVpnDialupVdom_Type = FnVdIndex
_FnVpnDialupVdom_Object = MibTableColumn
fnVpnDialupVdom = _FnVpnDialupVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 8),
    _FnVpnDialupVdom_Type()
)
fnVpnDialupVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupVdom.setStatus("current")
_FnVpnDialupInOctets_Type = Counter64
_FnVpnDialupInOctets_Object = MibTableColumn
fnVpnDialupInOctets = _FnVpnDialupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 9),
    _FnVpnDialupInOctets_Type()
)
fnVpnDialupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupInOctets.setStatus("current")
_FnVpnDialupOutOctets_Type = Counter64
_FnVpnDialupOutOctets_Object = MibTableColumn
fnVpnDialupOutOctets = _FnVpnDialupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 1, 1, 10),
    _FnVpnDialupOutOctets_Type()
)
fnVpnDialupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnDialupOutOctets.setStatus("current")
_FnVpnTrapLocalGateway_Type = IpAddress
_FnVpnTrapLocalGateway_Object = MibScalar
fnVpnTrapLocalGateway = _FnVpnTrapLocalGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 2),
    _FnVpnTrapLocalGateway_Type()
)
fnVpnTrapLocalGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnVpnTrapLocalGateway.setStatus("current")
_FnVpnTrapRemoteGateway_Type = IpAddress
_FnVpnTrapRemoteGateway_Object = MibScalar
fnVpnTrapRemoteGateway = _FnVpnTrapRemoteGateway_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 3),
    _FnVpnTrapRemoteGateway_Type()
)
fnVpnTrapRemoteGateway.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnVpnTrapRemoteGateway.setStatus("current")
_FnVpnTunTable_Object = MibTable
fnVpnTunTable = _FnVpnTunTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4)
)
if mibBuilder.loadTexts:
    fnVpnTunTable.setStatus("current")
_FnVpnTunEntry_Object = MibTableRow
fnVpnTunEntry = _FnVpnTunEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1)
)
fnVpnTunEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnVpnTunEntIndex"),
)
if mibBuilder.loadTexts:
    fnVpnTunEntry.setStatus("current")
_FnVpnTunEntIndex_Type = FnIndex
_FnVpnTunEntIndex_Object = MibTableColumn
fnVpnTunEntIndex = _FnVpnTunEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 1),
    _FnVpnTunEntIndex_Type()
)
fnVpnTunEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnTunEntIndex.setStatus("current")
_FnVpnTunEntPhase1Name_Type = DisplayString
_FnVpnTunEntPhase1Name_Object = MibTableColumn
fnVpnTunEntPhase1Name = _FnVpnTunEntPhase1Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 2),
    _FnVpnTunEntPhase1Name_Type()
)
fnVpnTunEntPhase1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntPhase1Name.setStatus("current")
_FnVpnTunEntPhase2Name_Type = DisplayString
_FnVpnTunEntPhase2Name_Object = MibTableColumn
fnVpnTunEntPhase2Name = _FnVpnTunEntPhase2Name_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 3),
    _FnVpnTunEntPhase2Name_Type()
)
fnVpnTunEntPhase2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntPhase2Name.setStatus("current")
_FnVpnTunEntRemGwyIp_Type = IpAddress
_FnVpnTunEntRemGwyIp_Object = MibTableColumn
fnVpnTunEntRemGwyIp = _FnVpnTunEntRemGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 4),
    _FnVpnTunEntRemGwyIp_Type()
)
fnVpnTunEntRemGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntRemGwyIp.setStatus("current")
_FnVpnTunEntRemGwyPort_Type = InetPortNumber
_FnVpnTunEntRemGwyPort_Object = MibTableColumn
fnVpnTunEntRemGwyPort = _FnVpnTunEntRemGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 5),
    _FnVpnTunEntRemGwyPort_Type()
)
fnVpnTunEntRemGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntRemGwyPort.setStatus("current")
_FnVpnTunEntLocGwyIp_Type = IpAddress
_FnVpnTunEntLocGwyIp_Object = MibTableColumn
fnVpnTunEntLocGwyIp = _FnVpnTunEntLocGwyIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 6),
    _FnVpnTunEntLocGwyIp_Type()
)
fnVpnTunEntLocGwyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntLocGwyIp.setStatus("current")
_FnVpnTunEntLocGwyPort_Type = InetPortNumber
_FnVpnTunEntLocGwyPort_Object = MibTableColumn
fnVpnTunEntLocGwyPort = _FnVpnTunEntLocGwyPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 7),
    _FnVpnTunEntLocGwyPort_Type()
)
fnVpnTunEntLocGwyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntLocGwyPort.setStatus("current")
_FnVpnTunEntSelectorSrcBeginIp_Type = IpAddress
_FnVpnTunEntSelectorSrcBeginIp_Object = MibTableColumn
fnVpnTunEntSelectorSrcBeginIp = _FnVpnTunEntSelectorSrcBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 8),
    _FnVpnTunEntSelectorSrcBeginIp_Type()
)
fnVpnTunEntSelectorSrcBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntSelectorSrcBeginIp.setStatus("current")
_FnVpnTunEntSelectorSrcEndIp_Type = IpAddress
_FnVpnTunEntSelectorSrcEndIp_Object = MibTableColumn
fnVpnTunEntSelectorSrcEndIp = _FnVpnTunEntSelectorSrcEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 9),
    _FnVpnTunEntSelectorSrcEndIp_Type()
)
fnVpnTunEntSelectorSrcEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntSelectorSrcEndIp.setStatus("current")
_FnVpnTunEntSelectorSrcPort_Type = InetPortNumber
_FnVpnTunEntSelectorSrcPort_Object = MibTableColumn
fnVpnTunEntSelectorSrcPort = _FnVpnTunEntSelectorSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 10),
    _FnVpnTunEntSelectorSrcPort_Type()
)
fnVpnTunEntSelectorSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntSelectorSrcPort.setStatus("current")
_FnVpnTunEntSelectorDstBeginIp_Type = IpAddress
_FnVpnTunEntSelectorDstBeginIp_Object = MibTableColumn
fnVpnTunEntSelectorDstBeginIp = _FnVpnTunEntSelectorDstBeginIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 11),
    _FnVpnTunEntSelectorDstBeginIp_Type()
)
fnVpnTunEntSelectorDstBeginIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntSelectorDstBeginIp.setStatus("current")
_FnVpnTunEntSelectorDstEndIp_Type = IpAddress
_FnVpnTunEntSelectorDstEndIp_Object = MibTableColumn
fnVpnTunEntSelectorDstEndIp = _FnVpnTunEntSelectorDstEndIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 12),
    _FnVpnTunEntSelectorDstEndIp_Type()
)
fnVpnTunEntSelectorDstEndIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntSelectorDstEndIp.setStatus("current")
_FnVpnTunEntSelectorDstPort_Type = InetPortNumber
_FnVpnTunEntSelectorDstPort_Object = MibTableColumn
fnVpnTunEntSelectorDstPort = _FnVpnTunEntSelectorDstPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 13),
    _FnVpnTunEntSelectorDstPort_Type()
)
fnVpnTunEntSelectorDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntSelectorDstPort.setStatus("current")
_FnVpnTunEntSelectorProto_Type = Integer32
_FnVpnTunEntSelectorProto_Object = MibTableColumn
fnVpnTunEntSelectorProto = _FnVpnTunEntSelectorProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 14),
    _FnVpnTunEntSelectorProto_Type()
)
fnVpnTunEntSelectorProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntSelectorProto.setStatus("current")
_FnVpnTunEntLifeSecs_Type = Gauge32
_FnVpnTunEntLifeSecs_Object = MibTableColumn
fnVpnTunEntLifeSecs = _FnVpnTunEntLifeSecs_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 15),
    _FnVpnTunEntLifeSecs_Type()
)
fnVpnTunEntLifeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntLifeSecs.setStatus("current")
_FnVpnTunEntLifeBytes_Type = Gauge32
_FnVpnTunEntLifeBytes_Object = MibTableColumn
fnVpnTunEntLifeBytes = _FnVpnTunEntLifeBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 16),
    _FnVpnTunEntLifeBytes_Type()
)
fnVpnTunEntLifeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntLifeBytes.setStatus("current")
_FnVpnTunEntTimeout_Type = Gauge32
_FnVpnTunEntTimeout_Object = MibTableColumn
fnVpnTunEntTimeout = _FnVpnTunEntTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 17),
    _FnVpnTunEntTimeout_Type()
)
fnVpnTunEntTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntTimeout.setStatus("current")
_FnVpnTunEntInOctets_Type = Counter64
_FnVpnTunEntInOctets_Object = MibTableColumn
fnVpnTunEntInOctets = _FnVpnTunEntInOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 18),
    _FnVpnTunEntInOctets_Type()
)
fnVpnTunEntInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntInOctets.setStatus("current")
_FnVpnTunEntOutOctets_Type = Counter64
_FnVpnTunEntOutOctets_Object = MibTableColumn
fnVpnTunEntOutOctets = _FnVpnTunEntOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 19),
    _FnVpnTunEntOutOctets_Type()
)
fnVpnTunEntOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntOutOctets.setStatus("current")


class _FnVpnTunEntStatus_Type(Integer32):
    """Custom type fnVpnTunEntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_FnVpnTunEntStatus_Type.__name__ = "Integer32"
_FnVpnTunEntStatus_Object = MibTableColumn
fnVpnTunEntStatus = _FnVpnTunEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 20),
    _FnVpnTunEntStatus_Type()
)
fnVpnTunEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntStatus.setStatus("current")
_FnVpnTunEntVdom_Type = FnVdIndex
_FnVpnTunEntVdom_Object = MibTableColumn
fnVpnTunEntVdom = _FnVpnTunEntVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 4, 1, 21),
    _FnVpnTunEntVdom_Type()
)
fnVpnTunEntVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnTunEntVdom.setStatus("current")
_FnVpnSslStatsTable_Object = MibTable
fnVpnSslStatsTable = _FnVpnSslStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5)
)
if mibBuilder.loadTexts:
    fnVpnSslStatsTable.setStatus("current")
_FnVpnSslStatsEntry_Object = MibTableRow
fnVpnSslStatsEntry = _FnVpnSslStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1)
)
fnVpnSslStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnVpnSslStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnVpnSslStatsEntry.setStatus("current")
_FnVpnSslStatsVdomIndex_Type = FnVdIndex
_FnVpnSslStatsVdomIndex_Object = MibTableColumn
fnVpnSslStatsVdomIndex = _FnVpnSslStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 1),
    _FnVpnSslStatsVdomIndex_Type()
)
fnVpnSslStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnSslStatsVdomIndex.setStatus("current")
_FnVpnSslState_Type = FnBoolState
_FnVpnSslState_Object = MibTableColumn
fnVpnSslState = _FnVpnSslState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 2),
    _FnVpnSslState_Type()
)
fnVpnSslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslState.setStatus("current")
_FnVpnSslStatsLoginUsers_Type = Counter32
_FnVpnSslStatsLoginUsers_Object = MibTableColumn
fnVpnSslStatsLoginUsers = _FnVpnSslStatsLoginUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 3),
    _FnVpnSslStatsLoginUsers_Type()
)
fnVpnSslStatsLoginUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslStatsLoginUsers.setStatus("current")
_FnVpnSslStatsMaxUsers_Type = Counter32
_FnVpnSslStatsMaxUsers_Object = MibTableColumn
fnVpnSslStatsMaxUsers = _FnVpnSslStatsMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 4),
    _FnVpnSslStatsMaxUsers_Type()
)
fnVpnSslStatsMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslStatsMaxUsers.setStatus("current")
_FnVpnSslStatsActiveWebSessions_Type = Counter32
_FnVpnSslStatsActiveWebSessions_Object = MibTableColumn
fnVpnSslStatsActiveWebSessions = _FnVpnSslStatsActiveWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 5),
    _FnVpnSslStatsActiveWebSessions_Type()
)
fnVpnSslStatsActiveWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslStatsActiveWebSessions.setStatus("current")
_FnVpnSslStatsMaxWebSessions_Type = Counter32
_FnVpnSslStatsMaxWebSessions_Object = MibTableColumn
fnVpnSslStatsMaxWebSessions = _FnVpnSslStatsMaxWebSessions_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 6),
    _FnVpnSslStatsMaxWebSessions_Type()
)
fnVpnSslStatsMaxWebSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslStatsMaxWebSessions.setStatus("current")
_FnVpnSslStatsActiveTunnels_Type = Counter32
_FnVpnSslStatsActiveTunnels_Object = MibTableColumn
fnVpnSslStatsActiveTunnels = _FnVpnSslStatsActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 7),
    _FnVpnSslStatsActiveTunnels_Type()
)
fnVpnSslStatsActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslStatsActiveTunnels.setStatus("current")
_FnVpnSslStatsMaxTunnels_Type = Counter32
_FnVpnSslStatsMaxTunnels_Object = MibTableColumn
fnVpnSslStatsMaxTunnels = _FnVpnSslStatsMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 5, 1, 8),
    _FnVpnSslStatsMaxTunnels_Type()
)
fnVpnSslStatsMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslStatsMaxTunnels.setStatus("current")
_FnVpnSslTunnelTable_Object = MibTable
fnVpnSslTunnelTable = _FnVpnSslTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6)
)
if mibBuilder.loadTexts:
    fnVpnSslTunnelTable.setStatus("current")
_FnVpnSslTunnelEntry_Object = MibTableRow
fnVpnSslTunnelEntry = _FnVpnSslTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1)
)
fnVpnSslTunnelEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnVpnSslTunnelIndex"),
)
if mibBuilder.loadTexts:
    fnVpnSslTunnelEntry.setStatus("current")
_FnVpnSslTunnelIndex_Type = FnIndex
_FnVpnSslTunnelIndex_Object = MibTableColumn
fnVpnSslTunnelIndex = _FnVpnSslTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 1),
    _FnVpnSslTunnelIndex_Type()
)
fnVpnSslTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnVpnSslTunnelIndex.setStatus("current")
_FnVpnSslTunnelVdom_Type = FnVdIndex
_FnVpnSslTunnelVdom_Object = MibTableColumn
fnVpnSslTunnelVdom = _FnVpnSslTunnelVdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 2),
    _FnVpnSslTunnelVdom_Type()
)
fnVpnSslTunnelVdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslTunnelVdom.setStatus("current")
_FnVpnSslTunnelUserName_Type = DisplayString
_FnVpnSslTunnelUserName_Object = MibTableColumn
fnVpnSslTunnelUserName = _FnVpnSslTunnelUserName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 3),
    _FnVpnSslTunnelUserName_Type()
)
fnVpnSslTunnelUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslTunnelUserName.setStatus("current")
_FnVpnSslTunnelSrcIp_Type = IpAddress
_FnVpnSslTunnelSrcIp_Object = MibTableColumn
fnVpnSslTunnelSrcIp = _FnVpnSslTunnelSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 4),
    _FnVpnSslTunnelSrcIp_Type()
)
fnVpnSslTunnelSrcIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslTunnelSrcIp.setStatus("current")
_FnVpnSslTunnelIp_Type = IpAddress
_FnVpnSslTunnelIp_Object = MibTableColumn
fnVpnSslTunnelIp = _FnVpnSslTunnelIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 5),
    _FnVpnSslTunnelIp_Type()
)
fnVpnSslTunnelIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslTunnelIp.setStatus("current")
_FnVpnSslTunnelUpTime_Type = Counter32
_FnVpnSslTunnelUpTime_Object = MibTableColumn
fnVpnSslTunnelUpTime = _FnVpnSslTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 6),
    _FnVpnSslTunnelUpTime_Type()
)
fnVpnSslTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslTunnelUpTime.setStatus("current")
_FnVpnSslTunnelBytesIn_Type = Counter64
_FnVpnSslTunnelBytesIn_Object = MibTableColumn
fnVpnSslTunnelBytesIn = _FnVpnSslTunnelBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 7),
    _FnVpnSslTunnelBytesIn_Type()
)
fnVpnSslTunnelBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslTunnelBytesIn.setStatus("current")
_FnVpnSslTunnelBytesOut_Type = Counter64
_FnVpnSslTunnelBytesOut_Object = MibTableColumn
fnVpnSslTunnelBytesOut = _FnVpnSslTunnelBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 12356, 9, 6, 1, 8),
    _FnVpnSslTunnelBytesOut_Type()
)
fnVpnSslTunnelBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVpnSslTunnelBytesOut.setStatus("current")
_FnManagement_ObjectIdentity = ObjectIdentity
fnManagement = _FnManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 10)
)


class _FnManSysSerial_Type(DisplayString):
    """Custom type fnManSysSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnManSysSerial_Type.__name__ = "DisplayString"
_FnManSysSerial_Object = MibScalar
fnManSysSerial = _FnManSysSerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 1),
    _FnManSysSerial_Type()
)
fnManSysSerial.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnManSysSerial.setStatus("current")
_FnManIfName_Type = DisplayString
_FnManIfName_Object = MibScalar
fnManIfName = _FnManIfName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 2),
    _FnManIfName_Type()
)
fnManIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnManIfName.setStatus("current")
_FnManIfIp_Type = IpAddress
_FnManIfIp_Object = MibScalar
fnManIfIp = _FnManIfIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 3),
    _FnManIfIp_Type()
)
fnManIfIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnManIfIp.setStatus("current")
_FnManIfMask_Type = IpAddress
_FnManIfMask_Object = MibScalar
fnManIfMask = _FnManIfMask_Object(
    (1, 3, 6, 1, 4, 1, 12356, 10, 4),
    _FnManIfMask_Type()
)
fnManIfMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnManIfMask.setStatus("current")
_FnAntivirus_ObjectIdentity = ObjectIdentity
fnAntivirus = _FnAntivirus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 11)
)
_FnAvTrapVirName_Type = DisplayString
_FnAvTrapVirName_Object = MibScalar
fnAvTrapVirName = _FnAvTrapVirName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 1),
    _FnAvTrapVirName_Type()
)
fnAvTrapVirName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnAvTrapVirName.setStatus("current")
_FnAvStatsTable_Object = MibTable
fnAvStatsTable = _FnAvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2)
)
if mibBuilder.loadTexts:
    fnAvStatsTable.setStatus("current")
_FnAvStatsEntry_Object = MibTableRow
fnAvStatsEntry = _FnAvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1)
)
fnAvStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnAvStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnAvStatsEntry.setStatus("current")
_FnAvStatsVdomIndex_Type = FnVdIndex
_FnAvStatsVdomIndex_Object = MibTableColumn
fnAvStatsVdomIndex = _FnAvStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 1),
    _FnAvStatsVdomIndex_Type()
)
fnAvStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAvStatsVdomIndex.setStatus("current")
_FnAvVirusDetected_Type = Counter32
_FnAvVirusDetected_Object = MibTableColumn
fnAvVirusDetected = _FnAvVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 2),
    _FnAvVirusDetected_Type()
)
fnAvVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvVirusDetected.setStatus("current")
_FnAvVirusBlocked_Type = Counter32
_FnAvVirusBlocked_Object = MibTableColumn
fnAvVirusBlocked = _FnAvVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 3),
    _FnAvVirusBlocked_Type()
)
fnAvVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvVirusBlocked.setStatus("current")
_FnAvHTTPVirusDetected_Type = Counter32
_FnAvHTTPVirusDetected_Object = MibTableColumn
fnAvHTTPVirusDetected = _FnAvHTTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 4),
    _FnAvHTTPVirusDetected_Type()
)
fnAvHTTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvHTTPVirusDetected.setStatus("current")
_FnAvHTTPVirusBlocked_Type = Counter32
_FnAvHTTPVirusBlocked_Object = MibTableColumn
fnAvHTTPVirusBlocked = _FnAvHTTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 5),
    _FnAvHTTPVirusBlocked_Type()
)
fnAvHTTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvHTTPVirusBlocked.setStatus("current")
_FnAvSMTPVirusDetected_Type = Counter32
_FnAvSMTPVirusDetected_Object = MibTableColumn
fnAvSMTPVirusDetected = _FnAvSMTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 6),
    _FnAvSMTPVirusDetected_Type()
)
fnAvSMTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvSMTPVirusDetected.setStatus("current")
_FnAvSMTPVirusBlocked_Type = Counter32
_FnAvSMTPVirusBlocked_Object = MibTableColumn
fnAvSMTPVirusBlocked = _FnAvSMTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 7),
    _FnAvSMTPVirusBlocked_Type()
)
fnAvSMTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvSMTPVirusBlocked.setStatus("current")
_FnAvPOP3VirusDetected_Type = Counter32
_FnAvPOP3VirusDetected_Object = MibTableColumn
fnAvPOP3VirusDetected = _FnAvPOP3VirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 8),
    _FnAvPOP3VirusDetected_Type()
)
fnAvPOP3VirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvPOP3VirusDetected.setStatus("current")
_FnAvPOP3VirusBlocked_Type = Counter32
_FnAvPOP3VirusBlocked_Object = MibTableColumn
fnAvPOP3VirusBlocked = _FnAvPOP3VirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 9),
    _FnAvPOP3VirusBlocked_Type()
)
fnAvPOP3VirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvPOP3VirusBlocked.setStatus("current")
_FnAvIMAPVirusDetected_Type = Counter32
_FnAvIMAPVirusDetected_Object = MibTableColumn
fnAvIMAPVirusDetected = _FnAvIMAPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 10),
    _FnAvIMAPVirusDetected_Type()
)
fnAvIMAPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvIMAPVirusDetected.setStatus("current")
_FnAvIMAPVirusBlocked_Type = Counter32
_FnAvIMAPVirusBlocked_Object = MibTableColumn
fnAvIMAPVirusBlocked = _FnAvIMAPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 11),
    _FnAvIMAPVirusBlocked_Type()
)
fnAvIMAPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvIMAPVirusBlocked.setStatus("current")
_FnAvFTPVirusDetected_Type = Counter32
_FnAvFTPVirusDetected_Object = MibTableColumn
fnAvFTPVirusDetected = _FnAvFTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 12),
    _FnAvFTPVirusDetected_Type()
)
fnAvFTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFTPVirusDetected.setStatus("current")
_FnAvFTPVirusBlocked_Type = Counter32
_FnAvFTPVirusBlocked_Object = MibTableColumn
fnAvFTPVirusBlocked = _FnAvFTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 13),
    _FnAvFTPVirusBlocked_Type()
)
fnAvFTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvFTPVirusBlocked.setStatus("current")
_FnAvIMVirusDetected_Type = Counter32
_FnAvIMVirusDetected_Object = MibTableColumn
fnAvIMVirusDetected = _FnAvIMVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 14),
    _FnAvIMVirusDetected_Type()
)
fnAvIMVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvIMVirusDetected.setStatus("current")
_FnAvIMVirusBlocked_Type = Counter32
_FnAvIMVirusBlocked_Object = MibTableColumn
fnAvIMVirusBlocked = _FnAvIMVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 15),
    _FnAvIMVirusBlocked_Type()
)
fnAvIMVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvIMVirusBlocked.setStatus("current")
_FnAvNNTPVirusDetected_Type = Counter32
_FnAvNNTPVirusDetected_Object = MibTableColumn
fnAvNNTPVirusDetected = _FnAvNNTPVirusDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 16),
    _FnAvNNTPVirusDetected_Type()
)
fnAvNNTPVirusDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvNNTPVirusDetected.setStatus("current")
_FnAvNNTPVirusBlocked_Type = Counter32
_FnAvNNTPVirusBlocked_Object = MibTableColumn
fnAvNNTPVirusBlocked = _FnAvNNTPVirusBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 17),
    _FnAvNNTPVirusBlocked_Type()
)
fnAvNNTPVirusBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvNNTPVirusBlocked.setStatus("current")
_FnAvOversizedDetected_Type = Counter32
_FnAvOversizedDetected_Object = MibTableColumn
fnAvOversizedDetected = _FnAvOversizedDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 18),
    _FnAvOversizedDetected_Type()
)
fnAvOversizedDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvOversizedDetected.setStatus("current")
_FnAvOversizedBlocked_Type = Counter32
_FnAvOversizedBlocked_Object = MibTableColumn
fnAvOversizedBlocked = _FnAvOversizedBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 11, 2, 1, 19),
    _FnAvOversizedBlocked_Type()
)
fnAvOversizedBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAvOversizedBlocked.setStatus("current")
_FnWebfilter_ObjectIdentity = ObjectIdentity
fnWebfilter = _FnWebfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 13)
)
_FnWebfilterStatsTable_Object = MibTable
fnWebfilterStatsTable = _FnWebfilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1)
)
if mibBuilder.loadTexts:
    fnWebfilterStatsTable.setStatus("current")
_FnWebfilterStatsEntry_Object = MibTableRow
fnWebfilterStatsEntry = _FnWebfilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1)
)
fnWebfilterStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnWfStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnWebfilterStatsEntry.setStatus("current")
_FnWfStatsVdomIndex_Type = FnVdIndex
_FnWfStatsVdomIndex_Object = MibTableColumn
fnWfStatsVdomIndex = _FnWfStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 1),
    _FnWfStatsVdomIndex_Type()
)
fnWfStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnWfStatsVdomIndex.setStatus("current")
_FnWfHTTPBlocked_Type = Counter32
_FnWfHTTPBlocked_Object = MibTableColumn
fnWfHTTPBlocked = _FnWfHTTPBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 2),
    _FnWfHTTPBlocked_Type()
)
fnWfHTTPBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfHTTPBlocked.setStatus("current")
_FnWfHTTPSBlocked_Type = Counter32
_FnWfHTTPSBlocked_Object = MibTableColumn
fnWfHTTPSBlocked = _FnWfHTTPSBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 3),
    _FnWfHTTPSBlocked_Type()
)
fnWfHTTPSBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfHTTPSBlocked.setStatus("current")
_FnWfHTTPURLBlocked_Type = Counter32
_FnWfHTTPURLBlocked_Object = MibTableColumn
fnWfHTTPURLBlocked = _FnWfHTTPURLBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 4),
    _FnWfHTTPURLBlocked_Type()
)
fnWfHTTPURLBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfHTTPURLBlocked.setStatus("current")
_FnWfHTTPSURLBlocked_Type = Counter32
_FnWfHTTPSURLBlocked_Object = MibTableColumn
fnWfHTTPSURLBlocked = _FnWfHTTPSURLBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 5),
    _FnWfHTTPSURLBlocked_Type()
)
fnWfHTTPSURLBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfHTTPSURLBlocked.setStatus("current")
_FnWfActiveXBlocked_Type = Counter32
_FnWfActiveXBlocked_Object = MibTableColumn
fnWfActiveXBlocked = _FnWfActiveXBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 6),
    _FnWfActiveXBlocked_Type()
)
fnWfActiveXBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfActiveXBlocked.setStatus("current")
_FnWfCookieBlocked_Type = Counter32
_FnWfCookieBlocked_Object = MibTableColumn
fnWfCookieBlocked = _FnWfCookieBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 7),
    _FnWfCookieBlocked_Type()
)
fnWfCookieBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfCookieBlocked.setStatus("current")
_FnWfAppletBlocked_Type = Counter32
_FnWfAppletBlocked_Object = MibTableColumn
fnWfAppletBlocked = _FnWfAppletBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 1, 1, 8),
    _FnWfAppletBlocked_Type()
)
fnWfAppletBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnWfAppletBlocked.setStatus("current")
_FnFortiGuardStatsTable_Object = MibTable
fnFortiGuardStatsTable = _FnFortiGuardStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2)
)
if mibBuilder.loadTexts:
    fnFortiGuardStatsTable.setStatus("current")
_FnFortiGuardStatsEntry_Object = MibTableRow
fnFortiGuardStatsEntry = _FnFortiGuardStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1)
)
fnFortiGuardStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnFgWfStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnFortiGuardStatsEntry.setStatus("current")
_FnFgWfStatsVdomIndex_Type = FnVdIndex
_FnFgWfStatsVdomIndex_Object = MibTableColumn
fnFgWfStatsVdomIndex = _FnFgWfStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 1),
    _FnFgWfStatsVdomIndex_Type()
)
fnFgWfStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnFgWfStatsVdomIndex.setStatus("current")
_FnFgWfHTTPExamined_Type = Counter32
_FnFgWfHTTPExamined_Object = MibTableColumn
fnFgWfHTTPExamined = _FnFgWfHTTPExamined_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 2),
    _FnFgWfHTTPExamined_Type()
)
fnFgWfHTTPExamined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPExamined.setStatus("current")
_FnFgWfHTTPSExamined_Type = Counter32
_FnFgWfHTTPSExamined_Object = MibTableColumn
fnFgWfHTTPSExamined = _FnFgWfHTTPSExamined_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 3),
    _FnFgWfHTTPSExamined_Type()
)
fnFgWfHTTPSExamined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPSExamined.setStatus("current")
_FnFgWfHTTPAllowed_Type = Counter32
_FnFgWfHTTPAllowed_Object = MibTableColumn
fnFgWfHTTPAllowed = _FnFgWfHTTPAllowed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 4),
    _FnFgWfHTTPAllowed_Type()
)
fnFgWfHTTPAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPAllowed.setStatus("current")
_FnFgWfHTTPSAllowed_Type = Counter32
_FnFgWfHTTPSAllowed_Object = MibTableColumn
fnFgWfHTTPSAllowed = _FnFgWfHTTPSAllowed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 5),
    _FnFgWfHTTPSAllowed_Type()
)
fnFgWfHTTPSAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPSAllowed.setStatus("current")
_FnFgWfHTTPBlocked_Type = Counter32
_FnFgWfHTTPBlocked_Object = MibTableColumn
fnFgWfHTTPBlocked = _FnFgWfHTTPBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 6),
    _FnFgWfHTTPBlocked_Type()
)
fnFgWfHTTPBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPBlocked.setStatus("current")
_FnFgWfHTTPSBlocked_Type = Counter32
_FnFgWfHTTPSBlocked_Object = MibTableColumn
fnFgWfHTTPSBlocked = _FnFgWfHTTPSBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 7),
    _FnFgWfHTTPSBlocked_Type()
)
fnFgWfHTTPSBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPSBlocked.setStatus("current")
_FnFgWfHTTPLogged_Type = Counter32
_FnFgWfHTTPLogged_Object = MibTableColumn
fnFgWfHTTPLogged = _FnFgWfHTTPLogged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 8),
    _FnFgWfHTTPLogged_Type()
)
fnFgWfHTTPLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPLogged.setStatus("current")
_FnFgWfHTTPSLogged_Type = Counter32
_FnFgWfHTTPSLogged_Object = MibTableColumn
fnFgWfHTTPSLogged = _FnFgWfHTTPSLogged_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 9),
    _FnFgWfHTTPSLogged_Type()
)
fnFgWfHTTPSLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPSLogged.setStatus("current")
_FnFgWfHTTPOverridden_Type = Counter32
_FnFgWfHTTPOverridden_Object = MibTableColumn
fnFgWfHTTPOverridden = _FnFgWfHTTPOverridden_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 10),
    _FnFgWfHTTPOverridden_Type()
)
fnFgWfHTTPOverridden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPOverridden.setStatus("current")
_FnFgWfHTTPSOverridden_Type = Counter32
_FnFgWfHTTPSOverridden_Object = MibTableColumn
fnFgWfHTTPSOverridden = _FnFgWfHTTPSOverridden_Object(
    (1, 3, 6, 1, 4, 1, 12356, 13, 2, 1, 11),
    _FnFgWfHTTPSOverridden_Type()
)
fnFgWfHTTPSOverridden.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnFgWfHTTPSOverridden.setStatus("current")
_FnIps_ObjectIdentity = ObjectIdentity
fnIps = _FnIps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 16)
)
_FnIpsTrapSigId_Type = FnIndex
_FnIpsTrapSigId_Object = MibScalar
fnIpsTrapSigId = _FnIpsTrapSigId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 1),
    _FnIpsTrapSigId_Type()
)
fnIpsTrapSigId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnIpsTrapSigId.setStatus("current")
_FnIpsTrapSrcIp_Type = IpAddress
_FnIpsTrapSrcIp_Object = MibScalar
fnIpsTrapSrcIp = _FnIpsTrapSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 2),
    _FnIpsTrapSrcIp_Type()
)
fnIpsTrapSrcIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnIpsTrapSrcIp.setStatus("current")
_FnIpsTrapSigMsg_Type = DisplayString
_FnIpsTrapSigMsg_Object = MibScalar
fnIpsTrapSigMsg = _FnIpsTrapSigMsg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 3),
    _FnIpsTrapSigMsg_Type()
)
fnIpsTrapSigMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fnIpsTrapSigMsg.setStatus("current")
_FnIpsStatsTable_Object = MibTable
fnIpsStatsTable = _FnIpsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4)
)
if mibBuilder.loadTexts:
    fnIpsStatsTable.setStatus("current")
_FnIpsStatsEntry_Object = MibTableRow
fnIpsStatsEntry = _FnIpsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1)
)
fnIpsStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnIpsStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnIpsStatsEntry.setStatus("current")
_FnIpsStatsVdomIndex_Type = FnVdIndex
_FnIpsStatsVdomIndex_Object = MibTableColumn
fnIpsStatsVdomIndex = _FnIpsStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 1),
    _FnIpsStatsVdomIndex_Type()
)
fnIpsStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnIpsStatsVdomIndex.setStatus("current")
_FnIpsIntrusionsDetected_Type = Counter32
_FnIpsIntrusionsDetected_Object = MibTableColumn
fnIpsIntrusionsDetected = _FnIpsIntrusionsDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 2),
    _FnIpsIntrusionsDetected_Type()
)
fnIpsIntrusionsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsIntrusionsDetected.setStatus("current")
_FnIpsIntrusionsBlocked_Type = Counter32
_FnIpsIntrusionsBlocked_Object = MibTableColumn
fnIpsIntrusionsBlocked = _FnIpsIntrusionsBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 3),
    _FnIpsIntrusionsBlocked_Type()
)
fnIpsIntrusionsBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsIntrusionsBlocked.setStatus("current")
_FnIpsCritSevDetections_Type = Counter32
_FnIpsCritSevDetections_Object = MibTableColumn
fnIpsCritSevDetections = _FnIpsCritSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 4),
    _FnIpsCritSevDetections_Type()
)
fnIpsCritSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsCritSevDetections.setStatus("current")
_FnIpsHighSevDetections_Type = Counter32
_FnIpsHighSevDetections_Object = MibTableColumn
fnIpsHighSevDetections = _FnIpsHighSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 5),
    _FnIpsHighSevDetections_Type()
)
fnIpsHighSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsHighSevDetections.setStatus("current")
_FnIpsMedSevDetections_Type = Counter32
_FnIpsMedSevDetections_Object = MibTableColumn
fnIpsMedSevDetections = _FnIpsMedSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 6),
    _FnIpsMedSevDetections_Type()
)
fnIpsMedSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsMedSevDetections.setStatus("current")
_FnIpsLowSevDetections_Type = Counter32
_FnIpsLowSevDetections_Object = MibTableColumn
fnIpsLowSevDetections = _FnIpsLowSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 7),
    _FnIpsLowSevDetections_Type()
)
fnIpsLowSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsLowSevDetections.setStatus("current")
_FnIpsInfoSevDetections_Type = Counter32
_FnIpsInfoSevDetections_Object = MibTableColumn
fnIpsInfoSevDetections = _FnIpsInfoSevDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 8),
    _FnIpsInfoSevDetections_Type()
)
fnIpsInfoSevDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsInfoSevDetections.setStatus("current")
_FnIpsSignatureDetections_Type = Counter32
_FnIpsSignatureDetections_Object = MibTableColumn
fnIpsSignatureDetections = _FnIpsSignatureDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 9),
    _FnIpsSignatureDetections_Type()
)
fnIpsSignatureDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsSignatureDetections.setStatus("current")
_FnIpsAnomalyDetections_Type = Counter32
_FnIpsAnomalyDetections_Object = MibTableColumn
fnIpsAnomalyDetections = _FnIpsAnomalyDetections_Object(
    (1, 3, 6, 1, 4, 1, 12356, 16, 4, 1, 10),
    _FnIpsAnomalyDetections_Type()
)
fnIpsAnomalyDetections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnIpsAnomalyDetections.setStatus("current")
_FnApplications_ObjectIdentity = ObjectIdentity
fnApplications = _FnApplications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17)
)
_FnAppProxyHTTP_ObjectIdentity = ObjectIdentity
fnAppProxyHTTP = _FnAppProxyHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 100)
)
_FnApHTTPUpTime_Type = Counter32
_FnApHTTPUpTime_Object = MibScalar
fnApHTTPUpTime = _FnApHTTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 100, 1),
    _FnApHTTPUpTime_Type()
)
fnApHTTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApHTTPUpTime.setStatus("current")


class _FnApHTTPMemUsage_Type(Gauge32):
    """Custom type fnApHTTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApHTTPMemUsage_Type.__name__ = "Gauge32"
_FnApHTTPMemUsage_Object = MibScalar
fnApHTTPMemUsage = _FnApHTTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 100, 2),
    _FnApHTTPMemUsage_Type()
)
fnApHTTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApHTTPMemUsage.setStatus("current")
_FnApHTTPStatsTable_Object = MibTable
fnApHTTPStatsTable = _FnApHTTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 100, 3)
)
if mibBuilder.loadTexts:
    fnApHTTPStatsTable.setStatus("current")
_FnApHTTPStatsEntry_Object = MibTableRow
fnApHTTPStatsEntry = _FnApHTTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 100, 3, 1)
)
fnApHTTPStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApHTTPStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApHTTPStatsEntry.setStatus("current")
_FnApHTTPStatsVdomIndex_Type = FnVdIndex
_FnApHTTPStatsVdomIndex_Object = MibTableColumn
fnApHTTPStatsVdomIndex = _FnApHTTPStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 100, 3, 1, 1),
    _FnApHTTPStatsVdomIndex_Type()
)
fnApHTTPStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApHTTPStatsVdomIndex.setStatus("current")
_FnApHTTPReqProcessed_Type = Counter32
_FnApHTTPReqProcessed_Object = MibTableColumn
fnApHTTPReqProcessed = _FnApHTTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 100, 3, 1, 2),
    _FnApHTTPReqProcessed_Type()
)
fnApHTTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApHTTPReqProcessed.setStatus("current")
_FnAppProxySMTP_ObjectIdentity = ObjectIdentity
fnAppProxySMTP = _FnAppProxySMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101)
)
_FnApSMTPUpTime_Type = Counter32
_FnApSMTPUpTime_Object = MibScalar
fnApSMTPUpTime = _FnApSMTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101, 1),
    _FnApSMTPUpTime_Type()
)
fnApSMTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSMTPUpTime.setStatus("current")


class _FnApSMTPMemUsage_Type(Gauge32):
    """Custom type fnApSMTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApSMTPMemUsage_Type.__name__ = "Gauge32"
_FnApSMTPMemUsage_Object = MibScalar
fnApSMTPMemUsage = _FnApSMTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101, 2),
    _FnApSMTPMemUsage_Type()
)
fnApSMTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSMTPMemUsage.setStatus("current")
_FnApSMTPStatsTable_Object = MibTable
fnApSMTPStatsTable = _FnApSMTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101, 3)
)
if mibBuilder.loadTexts:
    fnApSMTPStatsTable.setStatus("current")
_FnApSMTPStatsEntry_Object = MibTableRow
fnApSMTPStatsEntry = _FnApSMTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101, 3, 1)
)
fnApSMTPStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApSMTPStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApSMTPStatsEntry.setStatus("current")
_FnApSMTPStatsVdomIndex_Type = FnVdIndex
_FnApSMTPStatsVdomIndex_Object = MibTableColumn
fnApSMTPStatsVdomIndex = _FnApSMTPStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101, 3, 1, 1),
    _FnApSMTPStatsVdomIndex_Type()
)
fnApSMTPStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApSMTPStatsVdomIndex.setStatus("current")
_FnApSMTPReqProcessed_Type = Counter32
_FnApSMTPReqProcessed_Object = MibTableColumn
fnApSMTPReqProcessed = _FnApSMTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101, 3, 1, 2),
    _FnApSMTPReqProcessed_Type()
)
fnApSMTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSMTPReqProcessed.setStatus("current")
_FnApSMTPSpamDetected_Type = Counter32
_FnApSMTPSpamDetected_Object = MibTableColumn
fnApSMTPSpamDetected = _FnApSMTPSpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 101, 3, 1, 3),
    _FnApSMTPSpamDetected_Type()
)
fnApSMTPSpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSMTPSpamDetected.setStatus("current")
_FnAppProxyPOP3_ObjectIdentity = ObjectIdentity
fnAppProxyPOP3 = _FnAppProxyPOP3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102)
)
_FnApPOP3UpTime_Type = Counter32
_FnApPOP3UpTime_Object = MibScalar
fnApPOP3UpTime = _FnApPOP3UpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102, 1),
    _FnApPOP3UpTime_Type()
)
fnApPOP3UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApPOP3UpTime.setStatus("current")


class _FnApPOP3MemUsage_Type(Gauge32):
    """Custom type fnApPOP3MemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApPOP3MemUsage_Type.__name__ = "Gauge32"
_FnApPOP3MemUsage_Object = MibScalar
fnApPOP3MemUsage = _FnApPOP3MemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102, 2),
    _FnApPOP3MemUsage_Type()
)
fnApPOP3MemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApPOP3MemUsage.setStatus("current")
_FnApPOP3StatsTable_Object = MibTable
fnApPOP3StatsTable = _FnApPOP3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102, 3)
)
if mibBuilder.loadTexts:
    fnApPOP3StatsTable.setStatus("current")
_FnApPOP3StatsEntry_Object = MibTableRow
fnApPOP3StatsEntry = _FnApPOP3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102, 3, 1)
)
fnApPOP3StatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApPOP3StatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApPOP3StatsEntry.setStatus("current")
_FnApPOP3StatsVdomIndex_Type = FnVdIndex
_FnApPOP3StatsVdomIndex_Object = MibTableColumn
fnApPOP3StatsVdomIndex = _FnApPOP3StatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102, 3, 1, 1),
    _FnApPOP3StatsVdomIndex_Type()
)
fnApPOP3StatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApPOP3StatsVdomIndex.setStatus("current")
_FnApPOP3ReqProcessed_Type = Counter32
_FnApPOP3ReqProcessed_Object = MibTableColumn
fnApPOP3ReqProcessed = _FnApPOP3ReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102, 3, 1, 2),
    _FnApPOP3ReqProcessed_Type()
)
fnApPOP3ReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApPOP3ReqProcessed.setStatus("current")
_FnApPOP3SpamDetected_Type = Counter32
_FnApPOP3SpamDetected_Object = MibTableColumn
fnApPOP3SpamDetected = _FnApPOP3SpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 102, 3, 1, 3),
    _FnApPOP3SpamDetected_Type()
)
fnApPOP3SpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApPOP3SpamDetected.setStatus("current")
_FnAppProxyIMAP_ObjectIdentity = ObjectIdentity
fnAppProxyIMAP = _FnAppProxyIMAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103)
)
_FnApIMAPUpTime_Type = Counter32
_FnApIMAPUpTime_Object = MibScalar
fnApIMAPUpTime = _FnApIMAPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103, 1),
    _FnApIMAPUpTime_Type()
)
fnApIMAPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApIMAPUpTime.setStatus("current")


class _FnApIMAPMemUsage_Type(Gauge32):
    """Custom type fnApIMAPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApIMAPMemUsage_Type.__name__ = "Gauge32"
_FnApIMAPMemUsage_Object = MibScalar
fnApIMAPMemUsage = _FnApIMAPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103, 2),
    _FnApIMAPMemUsage_Type()
)
fnApIMAPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApIMAPMemUsage.setStatus("current")
_FnApIMAPStatsTable_Object = MibTable
fnApIMAPStatsTable = _FnApIMAPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103, 3)
)
if mibBuilder.loadTexts:
    fnApIMAPStatsTable.setStatus("current")
_FnApIMAPStatsEntry_Object = MibTableRow
fnApIMAPStatsEntry = _FnApIMAPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103, 3, 1)
)
fnApIMAPStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApIMAPStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApIMAPStatsEntry.setStatus("current")
_FnApIMAPStatsVdomIndex_Type = FnVdIndex
_FnApIMAPStatsVdomIndex_Object = MibTableColumn
fnApIMAPStatsVdomIndex = _FnApIMAPStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103, 3, 1, 1),
    _FnApIMAPStatsVdomIndex_Type()
)
fnApIMAPStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApIMAPStatsVdomIndex.setStatus("current")
_FnApIMAPReqProcessed_Type = Counter32
_FnApIMAPReqProcessed_Object = MibTableColumn
fnApIMAPReqProcessed = _FnApIMAPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103, 3, 1, 2),
    _FnApIMAPReqProcessed_Type()
)
fnApIMAPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApIMAPReqProcessed.setStatus("current")
_FnApIMAPSpamDetected_Type = Counter32
_FnApIMAPSpamDetected_Object = MibTableColumn
fnApIMAPSpamDetected = _FnApIMAPSpamDetected_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 103, 3, 1, 3),
    _FnApIMAPSpamDetected_Type()
)
fnApIMAPSpamDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApIMAPSpamDetected.setStatus("current")
_FnAppProxyNNTP_ObjectIdentity = ObjectIdentity
fnAppProxyNNTP = _FnAppProxyNNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 104)
)
_FnApNNTPUpTime_Type = Counter32
_FnApNNTPUpTime_Object = MibScalar
fnApNNTPUpTime = _FnApNNTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 104, 1),
    _FnApNNTPUpTime_Type()
)
fnApNNTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApNNTPUpTime.setStatus("current")


class _FnApNNTPMemUsage_Type(Gauge32):
    """Custom type fnApNNTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApNNTPMemUsage_Type.__name__ = "Gauge32"
_FnApNNTPMemUsage_Object = MibScalar
fnApNNTPMemUsage = _FnApNNTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 104, 2),
    _FnApNNTPMemUsage_Type()
)
fnApNNTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApNNTPMemUsage.setStatus("current")
_FnApNNTPStatsTable_Object = MibTable
fnApNNTPStatsTable = _FnApNNTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 104, 3)
)
if mibBuilder.loadTexts:
    fnApNNTPStatsTable.setStatus("current")
_FnApNNTPStatsEntry_Object = MibTableRow
fnApNNTPStatsEntry = _FnApNNTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 104, 3, 1)
)
fnApNNTPStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApNNTPStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApNNTPStatsEntry.setStatus("current")
_FnApNNTPStatsVdomIndex_Type = FnVdIndex
_FnApNNTPStatsVdomIndex_Object = MibTableColumn
fnApNNTPStatsVdomIndex = _FnApNNTPStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 104, 3, 1, 1),
    _FnApNNTPStatsVdomIndex_Type()
)
fnApNNTPStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApNNTPStatsVdomIndex.setStatus("current")
_FnApNNTPReqProcessed_Type = Counter32
_FnApNNTPReqProcessed_Object = MibTableColumn
fnApNNTPReqProcessed = _FnApNNTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 104, 3, 1, 2),
    _FnApNNTPReqProcessed_Type()
)
fnApNNTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApNNTPReqProcessed.setStatus("current")
_FnAppProxyIM_ObjectIdentity = ObjectIdentity
fnAppProxyIM = _FnAppProxyIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 105)
)
_FnApIMUpTime_Type = Counter32
_FnApIMUpTime_Object = MibScalar
fnApIMUpTime = _FnApIMUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 105, 1),
    _FnApIMUpTime_Type()
)
fnApIMUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApIMUpTime.setStatus("current")


class _FnApIMMemUsage_Type(Gauge32):
    """Custom type fnApIMMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApIMMemUsage_Type.__name__ = "Gauge32"
_FnApIMMemUsage_Object = MibScalar
fnApIMMemUsage = _FnApIMMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 105, 2),
    _FnApIMMemUsage_Type()
)
fnApIMMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApIMMemUsage.setStatus("current")
_FnApIMStatsTable_Object = MibTable
fnApIMStatsTable = _FnApIMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 105, 3)
)
if mibBuilder.loadTexts:
    fnApIMStatsTable.setStatus("current")
_FnApIMStatsEntry_Object = MibTableRow
fnApIMStatsEntry = _FnApIMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 105, 3, 1)
)
fnApIMStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApIMStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApIMStatsEntry.setStatus("current")
_FnApIMStatsVdomIndex_Type = FnVdIndex
_FnApIMStatsVdomIndex_Object = MibTableColumn
fnApIMStatsVdomIndex = _FnApIMStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 105, 3, 1, 1),
    _FnApIMStatsVdomIndex_Type()
)
fnApIMStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApIMStatsVdomIndex.setStatus("current")
_FnApIMReqProcessed_Type = Counter32
_FnApIMReqProcessed_Object = MibTableColumn
fnApIMReqProcessed = _FnApIMReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 105, 3, 1, 2),
    _FnApIMReqProcessed_Type()
)
fnApIMReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApIMReqProcessed.setStatus("current")
_FnAppProxySIP_ObjectIdentity = ObjectIdentity
fnAppProxySIP = _FnAppProxySIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106)
)
_FnApSIPUpTime_Type = Counter32
_FnApSIPUpTime_Object = MibScalar
fnApSIPUpTime = _FnApSIPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 1),
    _FnApSIPUpTime_Type()
)
fnApSIPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSIPUpTime.setStatus("current")


class _FnApSIPMemUsage_Type(Gauge32):
    """Custom type fnApSIPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApSIPMemUsage_Type.__name__ = "Gauge32"
_FnApSIPMemUsage_Object = MibScalar
fnApSIPMemUsage = _FnApSIPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 2),
    _FnApSIPMemUsage_Type()
)
fnApSIPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSIPMemUsage.setStatus("current")
_FnApSIPStatsTable_Object = MibTable
fnApSIPStatsTable = _FnApSIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 3)
)
if mibBuilder.loadTexts:
    fnApSIPStatsTable.setStatus("current")
_FnApSIPStatsEntry_Object = MibTableRow
fnApSIPStatsEntry = _FnApSIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 3, 1)
)
fnApSIPStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApSIPStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApSIPStatsEntry.setStatus("current")
_FnApSIPStatsVdomIndex_Type = FnVdIndex
_FnApSIPStatsVdomIndex_Object = MibTableColumn
fnApSIPStatsVdomIndex = _FnApSIPStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 3, 1, 1),
    _FnApSIPStatsVdomIndex_Type()
)
fnApSIPStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApSIPStatsVdomIndex.setStatus("current")
_FnApSIPClientReg_Type = Counter32
_FnApSIPClientReg_Object = MibTableColumn
fnApSIPClientReg = _FnApSIPClientReg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 3, 1, 2),
    _FnApSIPClientReg_Type()
)
fnApSIPClientReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSIPClientReg.setStatus("current")
_FnApSIPCallHandling_Type = Counter32
_FnApSIPCallHandling_Object = MibTableColumn
fnApSIPCallHandling = _FnApSIPCallHandling_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 3, 1, 3),
    _FnApSIPCallHandling_Type()
)
fnApSIPCallHandling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSIPCallHandling.setStatus("current")
_FnApSIPServices_Type = Counter32
_FnApSIPServices_Object = MibTableColumn
fnApSIPServices = _FnApSIPServices_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 3, 1, 4),
    _FnApSIPServices_Type()
)
fnApSIPServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSIPServices.setStatus("current")
_FnApSIPOtherReq_Type = Counter32
_FnApSIPOtherReq_Object = MibTableColumn
fnApSIPOtherReq = _FnApSIPOtherReq_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 106, 3, 1, 5),
    _FnApSIPOtherReq_Type()
)
fnApSIPOtherReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApSIPOtherReq.setStatus("current")
_FnAppScanUnit_ObjectIdentity = ObjectIdentity
fnAppScanUnit = _FnAppScanUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 107)
)
_FnAppSuNumber_Type = Counter32
_FnAppSuNumber_Object = MibScalar
fnAppSuNumber = _FnAppSuNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 107, 1),
    _FnAppSuNumber_Type()
)
fnAppSuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppSuNumber.setStatus("current")
_FnAppSuStatsTable_Object = MibTable
fnAppSuStatsTable = _FnAppSuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 107, 2)
)
if mibBuilder.loadTexts:
    fnAppSuStatsTable.setStatus("current")
_FnAppSuStatsEntry_Object = MibTableRow
fnAppSuStatsEntry = _FnAppSuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 107, 2, 1)
)
fnAppSuStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnAppSuIndex"),
)
if mibBuilder.loadTexts:
    fnAppSuStatsEntry.setStatus("current")
_FnAppSuIndex_Type = FnIndex
_FnAppSuIndex_Object = MibTableColumn
fnAppSuIndex = _FnAppSuIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 107, 2, 1, 1),
    _FnAppSuIndex_Type()
)
fnAppSuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAppSuIndex.setStatus("current")
_FnAppSuFileScanned_Type = Counter32
_FnAppSuFileScanned_Object = MibTableColumn
fnAppSuFileScanned = _FnAppSuFileScanned_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 107, 2, 1, 2),
    _FnAppSuFileScanned_Type()
)
fnAppSuFileScanned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppSuFileScanned.setStatus("current")
_FnAppVoIP_ObjectIdentity = ObjectIdentity
fnAppVoIP = _FnAppVoIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 108)
)
_FnAppVoIPStatsTable_Object = MibTable
fnAppVoIPStatsTable = _FnAppVoIPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 108, 1)
)
if mibBuilder.loadTexts:
    fnAppVoIPStatsTable.setStatus("current")
_FnAppVoIPStatsEntry_Object = MibTableRow
fnAppVoIPStatsEntry = _FnAppVoIPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 108, 1, 1)
)
fnAppVoIPStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnAppVoIPStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnAppVoIPStatsEntry.setStatus("current")
_FnAppVoIPStatsVdomIndex_Type = FnVdIndex
_FnAppVoIPStatsVdomIndex_Object = MibTableColumn
fnAppVoIPStatsVdomIndex = _FnAppVoIPStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 108, 1, 1, 1),
    _FnAppVoIPStatsVdomIndex_Type()
)
fnAppVoIPStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAppVoIPStatsVdomIndex.setStatus("current")
_FnAppVoIPConn_Type = Counter32
_FnAppVoIPConn_Object = MibTableColumn
fnAppVoIPConn = _FnAppVoIPConn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 108, 1, 1, 2),
    _FnAppVoIPConn_Type()
)
fnAppVoIPConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppVoIPConn.setStatus("current")
_FnAppVoIPCallBlocked_Type = Counter32
_FnAppVoIPCallBlocked_Object = MibTableColumn
fnAppVoIPCallBlocked = _FnAppVoIPCallBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 108, 1, 1, 3),
    _FnAppVoIPCallBlocked_Type()
)
fnAppVoIPCallBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppVoIPCallBlocked.setStatus("current")
_FnAppP2P_ObjectIdentity = ObjectIdentity
fnAppP2P = _FnAppP2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109)
)
_FnAppP2PStatsTable_Object = MibTable
fnAppP2PStatsTable = _FnAppP2PStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 1)
)
if mibBuilder.loadTexts:
    fnAppP2PStatsTable.setStatus("current")
_FnAppP2PStatsEntry_Object = MibTableRow
fnAppP2PStatsEntry = _FnAppP2PStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 1, 1)
)
fnAppP2PStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnAppP2PStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnAppP2PStatsEntry.setStatus("current")
_FnAppP2PStatsVdomIndex_Type = FnVdIndex
_FnAppP2PStatsVdomIndex_Object = MibTableColumn
fnAppP2PStatsVdomIndex = _FnAppP2PStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 1, 1, 1),
    _FnAppP2PStatsVdomIndex_Type()
)
fnAppP2PStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAppP2PStatsVdomIndex.setStatus("current")
_FnAppP2PConnBlocked_Type = Counter32
_FnAppP2PConnBlocked_Object = MibTableColumn
fnAppP2PConnBlocked = _FnAppP2PConnBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 1, 1, 2),
    _FnAppP2PConnBlocked_Type()
)
fnAppP2PConnBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppP2PConnBlocked.setStatus("current")
_FnAppP2PProtoTable_Object = MibTable
fnAppP2PProtoTable = _FnAppP2PProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 2)
)
if mibBuilder.loadTexts:
    fnAppP2PProtoTable.setStatus("current")
_FnAppP2PProtoEntry_Object = MibTableRow
fnAppP2PProtoEntry = _FnAppP2PProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 2, 1)
)
fnAppP2PProtoEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnAppP2PProtEntVdIndex"),
    (0, "FORTIOS-300-MIB", "fnAppP2PProtEntProto"),
)
if mibBuilder.loadTexts:
    fnAppP2PProtoEntry.setStatus("current")
_FnAppP2PProtEntVdIndex_Type = FnVdIndex
_FnAppP2PProtEntVdIndex_Object = MibTableColumn
fnAppP2PProtEntVdIndex = _FnAppP2PProtEntVdIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 2, 1, 1),
    _FnAppP2PProtEntVdIndex_Type()
)
fnAppP2PProtEntVdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAppP2PProtEntVdIndex.setStatus("current")
_FnAppP2PProtEntProto_Type = FnP2PProto
_FnAppP2PProtEntProto_Object = MibTableColumn
fnAppP2PProtEntProto = _FnAppP2PProtEntProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 2, 1, 2),
    _FnAppP2PProtEntProto_Type()
)
fnAppP2PProtEntProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAppP2PProtEntProto.setStatus("current")
_FnAppP2PProtEntBytes_Type = Counter64
_FnAppP2PProtEntBytes_Object = MibTableColumn
fnAppP2PProtEntBytes = _FnAppP2PProtEntBytes_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 2, 1, 3),
    _FnAppP2PProtEntBytes_Type()
)
fnAppP2PProtEntBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppP2PProtEntBytes.setStatus("current")
_FnAppP2PProtoEntLastReset_Type = TimeTicks
_FnAppP2PProtoEntLastReset_Object = MibTableColumn
fnAppP2PProtoEntLastReset = _FnAppP2PProtoEntLastReset_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 109, 2, 1, 4),
    _FnAppP2PProtoEntLastReset_Type()
)
fnAppP2PProtoEntLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppP2PProtoEntLastReset.setStatus("current")
_FnAppIM_ObjectIdentity = ObjectIdentity
fnAppIM = _FnAppIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110)
)
_FnAppIMStatsTable_Object = MibTable
fnAppIMStatsTable = _FnAppIMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110, 1)
)
if mibBuilder.loadTexts:
    fnAppIMStatsTable.setStatus("current")
_FnAppIMStatsEntry_Object = MibTableRow
fnAppIMStatsEntry = _FnAppIMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110, 1, 1)
)
fnAppIMStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnAppIMStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnAppIMStatsEntry.setStatus("current")
_FnAppIMStatsVdomIndex_Type = FnVdIndex
_FnAppIMStatsVdomIndex_Object = MibTableColumn
fnAppIMStatsVdomIndex = _FnAppIMStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110, 1, 1, 1),
    _FnAppIMStatsVdomIndex_Type()
)
fnAppIMStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnAppIMStatsVdomIndex.setStatus("current")
_FnAppIMMessages_Type = Counter32
_FnAppIMMessages_Object = MibTableColumn
fnAppIMMessages = _FnAppIMMessages_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110, 1, 1, 2),
    _FnAppIMMessages_Type()
)
fnAppIMMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppIMMessages.setStatus("current")
_FnAppIMFileTransfered_Type = Counter32
_FnAppIMFileTransfered_Object = MibTableColumn
fnAppIMFileTransfered = _FnAppIMFileTransfered_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110, 1, 1, 3),
    _FnAppIMFileTransfered_Type()
)
fnAppIMFileTransfered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppIMFileTransfered.setStatus("current")
_FnAppIMFileTxBlocked_Type = Counter32
_FnAppIMFileTxBlocked_Object = MibTableColumn
fnAppIMFileTxBlocked = _FnAppIMFileTxBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110, 1, 1, 4),
    _FnAppIMFileTxBlocked_Type()
)
fnAppIMFileTxBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppIMFileTxBlocked.setStatus("current")
_FnAppIMConnBlocked_Type = Counter32
_FnAppIMConnBlocked_Object = MibTableColumn
fnAppIMConnBlocked = _FnAppIMConnBlocked_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 110, 1, 1, 5),
    _FnAppIMConnBlocked_Type()
)
fnAppIMConnBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnAppIMConnBlocked.setStatus("current")
_FnAppProxyFTP_ObjectIdentity = ObjectIdentity
fnAppProxyFTP = _FnAppProxyFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 17, 111)
)
_FnApFTPUpTime_Type = Counter32
_FnApFTPUpTime_Object = MibScalar
fnApFTPUpTime = _FnApFTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 111, 1),
    _FnApFTPUpTime_Type()
)
fnApFTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApFTPUpTime.setStatus("current")


class _FnApFTPMemUsage_Type(Gauge32):
    """Custom type fnApFTPMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FnApFTPMemUsage_Type.__name__ = "Gauge32"
_FnApFTPMemUsage_Object = MibScalar
fnApFTPMemUsage = _FnApFTPMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 111, 2),
    _FnApFTPMemUsage_Type()
)
fnApFTPMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApFTPMemUsage.setStatus("current")
_FnApFTPStatsTable_Object = MibTable
fnApFTPStatsTable = _FnApFTPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 111, 3)
)
if mibBuilder.loadTexts:
    fnApFTPStatsTable.setStatus("current")
_FnApFTPStatsEntry_Object = MibTableRow
fnApFTPStatsEntry = _FnApFTPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 111, 3, 1)
)
fnApFTPStatsEntry.setIndexNames(
    (0, "FORTIOS-300-MIB", "fnApFTPStatsVdomIndex"),
)
if mibBuilder.loadTexts:
    fnApFTPStatsEntry.setStatus("current")
_FnApFTPStatsVdomIndex_Type = FnVdIndex
_FnApFTPStatsVdomIndex_Object = MibTableColumn
fnApFTPStatsVdomIndex = _FnApFTPStatsVdomIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 111, 3, 1, 1),
    _FnApFTPStatsVdomIndex_Type()
)
fnApFTPStatsVdomIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fnApFTPStatsVdomIndex.setStatus("current")
_FnApFTPReqProcessed_Type = Counter32
_FnApFTPReqProcessed_Object = MibTableColumn
fnApFTPReqProcessed = _FnApFTPReqProcessed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 17, 111, 3, 1, 2),
    _FnApFTPReqProcessed_Type()
)
fnApFTPReqProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnApFTPReqProcessed.setStatus("current")
_FnMIBConformance_ObjectIdentity = ObjectIdentity
fnMIBConformance = _FnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 99)
)
ifEntry.registerAugmentions(
    ("FORTIOS-300-MIB",
     "fnIntfEntry")
)
fnIntfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

fnSystemComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 1)
)
fnSystemComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnSysModel"),
        ("FORTIOS-300-MIB", "fnSysSerial"),
        ("FORTIOS-300-MIB", "fnSysVersion"),
        ("FORTIOS-300-MIB", "fnSysVersionAv"),
        ("FORTIOS-300-MIB", "fnSysVersionNids"),
        ("FORTIOS-300-MIB", "fnSysHaMode"),
        ("FORTIOS-300-MIB", "fnSysOpMode"),
        ("FORTIOS-300-MIB", "fnSysCpuUsage"),
        ("FORTIOS-300-MIB", "fnSysMemUsage"),
        ("FORTIOS-300-MIB", "fnSysDiskCapacity"),
        ("FORTIOS-300-MIB", "fnSysDiskUsage"),
        ("FORTIOS-300-MIB", "fnSysMemCapacity"),
        ("FORTIOS-300-MIB", "fnSysSesCount"),
        ("FORTIOS-300-MIB", "fnOptIdleTimeout"),
        ("FORTIOS-300-MIB", "fnOptAuthTimeout"),
        ("FORTIOS-300-MIB", "fnOptLanguage"),
        ("FORTIOS-300-MIB", "fnOptLcdProtection"),
        ("FORTIOS-300-MIB", "fnVdNumber"),
        ("FORTIOS-300-MIB", "fnVdEntName"),
        ("FORTIOS-300-MIB", "fnVdEntOpMode"),
        ("FORTIOS-300-MIB", "fnVdMaxVdoms"),
        ("FORTIOS-300-MIB", "fnVdEnabled"))
)
if mibBuilder.loadTexts:
    fnSystemComplianceGroup.setStatus("current")

fnHaComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 2)
)
fnHaComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnHaGroupId"),
        ("FORTIOS-300-MIB", "fnHaPriority"),
        ("FORTIOS-300-MIB", "fnHaOverride"),
        ("FORTIOS-300-MIB", "fnHaAutoSync"),
        ("FORTIOS-300-MIB", "fnHaSchedule"),
        ("FORTIOS-300-MIB", "fnHaGroupName"),
        ("FORTIOS-300-MIB", "fnHaStatsSerial"),
        ("FORTIOS-300-MIB", "fnHaStatsCpuUsage"),
        ("FORTIOS-300-MIB", "fnHaStatsMemUsage"),
        ("FORTIOS-300-MIB", "fnHaStatsNetUsage"),
        ("FORTIOS-300-MIB", "fnHaStatsSesCount"),
        ("FORTIOS-300-MIB", "fnHaStatsPktCount"),
        ("FORTIOS-300-MIB", "fnHaStatsByteCount"),
        ("FORTIOS-300-MIB", "fnHaStatsIdsCount"),
        ("FORTIOS-300-MIB", "fnHaStatsAvCount"),
        ("FORTIOS-300-MIB", "fnHaStatsHostname"))
)
if mibBuilder.loadTexts:
    fnHaComplianceGroup.setStatus("current")

fnAuthComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 3)
)
fnAuthComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnAdminNumber"),
        ("FORTIOS-300-MIB", "fnAdminName"),
        ("FORTIOS-300-MIB", "fnAdminAddr"),
        ("FORTIOS-300-MIB", "fnAdminMask"),
        ("FORTIOS-300-MIB", "fnAdminVdom"),
        ("FORTIOS-300-MIB", "fnUserNumber"),
        ("FORTIOS-300-MIB", "fnUserName"),
        ("FORTIOS-300-MIB", "fnUserAuth"),
        ("FORTIOS-300-MIB", "fnUserState"),
        ("FORTIOS-300-MIB", "fnUserVdom"))
)
if mibBuilder.loadTexts:
    fnAuthComplianceGroup.setStatus("current")

fnSessionComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 4)
)
fnSessionComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnIpSessProto"),
        ("FORTIOS-300-MIB", "fnIpSessFromAddr"),
        ("FORTIOS-300-MIB", "fnIpSessFromPort"),
        ("FORTIOS-300-MIB", "fnIpSessToAddr"),
        ("FORTIOS-300-MIB", "fnIpSessToPort"),
        ("FORTIOS-300-MIB", "fnIpSessExp"),
        ("FORTIOS-300-MIB", "fnIpSessVdom"),
        ("FORTIOS-300-MIB", "fnIpSessNumber"))
)
if mibBuilder.loadTexts:
    fnSessionComplianceGroup.setStatus("current")

fnVPNComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 5)
)
fnVPNComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnVpnDialupGateway"),
        ("FORTIOS-300-MIB", "fnVpnDialupLifetime"),
        ("FORTIOS-300-MIB", "fnVpnDialupTimeout"),
        ("FORTIOS-300-MIB", "fnVpnDialupSrcBegin"),
        ("FORTIOS-300-MIB", "fnVpnDialupSrcEnd"),
        ("FORTIOS-300-MIB", "fnVpnDialupDstAddr"),
        ("FORTIOS-300-MIB", "fnVpnDialupVdom"),
        ("FORTIOS-300-MIB", "fnVpnDialupInOctets"),
        ("FORTIOS-300-MIB", "fnVpnDialupOutOctets"),
        ("FORTIOS-300-MIB", "fnVpnTunEntPhase1Name"),
        ("FORTIOS-300-MIB", "fnVpnTunEntPhase2Name"),
        ("FORTIOS-300-MIB", "fnVpnTunEntRemGwyIp"),
        ("FORTIOS-300-MIB", "fnVpnTunEntRemGwyPort"),
        ("FORTIOS-300-MIB", "fnVpnTunEntLocGwyIp"),
        ("FORTIOS-300-MIB", "fnVpnTunEntLocGwyPort"),
        ("FORTIOS-300-MIB", "fnVpnTunEntSelectorSrcBeginIp"),
        ("FORTIOS-300-MIB", "fnVpnTunEntSelectorSrcEndIp"),
        ("FORTIOS-300-MIB", "fnVpnTunEntSelectorSrcPort"),
        ("FORTIOS-300-MIB", "fnVpnTunEntSelectorDstBeginIp"),
        ("FORTIOS-300-MIB", "fnVpnTunEntSelectorDstEndIp"),
        ("FORTIOS-300-MIB", "fnVpnTunEntSelectorDstPort"),
        ("FORTIOS-300-MIB", "fnVpnTunEntSelectorProto"),
        ("FORTIOS-300-MIB", "fnVpnTunEntLifeSecs"),
        ("FORTIOS-300-MIB", "fnVpnTunEntLifeBytes"),
        ("FORTIOS-300-MIB", "fnVpnTunEntTimeout"),
        ("FORTIOS-300-MIB", "fnVpnTunEntInOctets"),
        ("FORTIOS-300-MIB", "fnVpnTunEntOutOctets"),
        ("FORTIOS-300-MIB", "fnVpnTunEntStatus"),
        ("FORTIOS-300-MIB", "fnVpnTunEntVdom"),
        ("FORTIOS-300-MIB", "fnVpnSslState"),
        ("FORTIOS-300-MIB", "fnVpnSslStatsLoginUsers"),
        ("FORTIOS-300-MIB", "fnVpnSslStatsMaxUsers"),
        ("FORTIOS-300-MIB", "fnVpnSslStatsActiveWebSessions"),
        ("FORTIOS-300-MIB", "fnVpnSslStatsMaxWebSessions"),
        ("FORTIOS-300-MIB", "fnVpnSslStatsActiveTunnels"),
        ("FORTIOS-300-MIB", "fnVpnSslStatsMaxTunnels"),
        ("FORTIOS-300-MIB", "fnVpnSslTunnelVdom"),
        ("FORTIOS-300-MIB", "fnVpnSslTunnelUserName"),
        ("FORTIOS-300-MIB", "fnVpnSslTunnelSrcIp"),
        ("FORTIOS-300-MIB", "fnVpnSslTunnelIp"),
        ("FORTIOS-300-MIB", "fnVpnSslTunnelUpTime"),
        ("FORTIOS-300-MIB", "fnVpnSslTunnelBytesIn"),
        ("FORTIOS-300-MIB", "fnVpnSslTunnelBytesOut"))
)
if mibBuilder.loadTexts:
    fnVPNComplianceGroup.setStatus("current")

fnManagementComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 9)
)
fnManagementComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnManSysSerial"),
        ("FORTIOS-300-MIB", "fnManIfName"),
        ("FORTIOS-300-MIB", "fnManIfIp"),
        ("FORTIOS-300-MIB", "fnManIfMask"))
)
if mibBuilder.loadTexts:
    fnManagementComplianceGroup.setStatus("current")

fnHwSensorsComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 10)
)
fnHwSensorsComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnHwSensorCount"),
        ("FORTIOS-300-MIB", "fnHwSensorEntName"),
        ("FORTIOS-300-MIB", "fnHwSensorEntValue"),
        ("FORTIOS-300-MIB", "fnHwSensorEntAlarmStatus"))
)
if mibBuilder.loadTexts:
    fnHwSensorsComplianceGroup.setStatus("current")

fnNotificationObjectsComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 11)
)
fnNotificationObjectsComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnAvTrapVirName"),
        ("FORTIOS-300-MIB", "fnIpsTrapSigId"),
        ("FORTIOS-300-MIB", "fnIpsTrapSrcIp"),
        ("FORTIOS-300-MIB", "fnIpsTrapSigMsg"),
        ("FORTIOS-300-MIB", "fnVpnTrapLocalGateway"),
        ("FORTIOS-300-MIB", "fnVpnTrapRemoteGateway"),
        ("FORTIOS-300-MIB", "fnHaTrapMemberSerial"),
        ("FORTIOS-300-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    fnNotificationObjectsComplianceGroup.setStatus("current")

fnAntivirusComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 12)
)
fnAntivirusComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnAvVirusDetected"),
        ("FORTIOS-300-MIB", "fnAvVirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvHTTPVirusDetected"),
        ("FORTIOS-300-MIB", "fnAvHTTPVirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvSMTPVirusDetected"),
        ("FORTIOS-300-MIB", "fnAvSMTPVirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvPOP3VirusDetected"),
        ("FORTIOS-300-MIB", "fnAvPOP3VirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvIMAPVirusDetected"),
        ("FORTIOS-300-MIB", "fnAvIMAPVirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvFTPVirusDetected"),
        ("FORTIOS-300-MIB", "fnAvFTPVirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvIMVirusDetected"),
        ("FORTIOS-300-MIB", "fnAvIMVirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvNNTPVirusDetected"),
        ("FORTIOS-300-MIB", "fnAvNNTPVirusBlocked"),
        ("FORTIOS-300-MIB", "fnAvOversizedDetected"),
        ("FORTIOS-300-MIB", "fnAvOversizedBlocked"))
)
if mibBuilder.loadTexts:
    fnAntivirusComplianceGroup.setStatus("current")

fnIpsComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 13)
)
fnIpsComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnIpsIntrusionsDetected"),
        ("FORTIOS-300-MIB", "fnIpsIntrusionsBlocked"),
        ("FORTIOS-300-MIB", "fnIpsCritSevDetections"),
        ("FORTIOS-300-MIB", "fnIpsHighSevDetections"),
        ("FORTIOS-300-MIB", "fnIpsMedSevDetections"),
        ("FORTIOS-300-MIB", "fnIpsLowSevDetections"),
        ("FORTIOS-300-MIB", "fnIpsInfoSevDetections"),
        ("FORTIOS-300-MIB", "fnIpsSignatureDetections"),
        ("FORTIOS-300-MIB", "fnIpsAnomalyDetections"))
)
if mibBuilder.loadTexts:
    fnIpsComplianceGroup.setStatus("current")

fnWebFilterComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 14)
)
fnWebFilterComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnWfHTTPBlocked"),
        ("FORTIOS-300-MIB", "fnWfHTTPSBlocked"),
        ("FORTIOS-300-MIB", "fnWfHTTPURLBlocked"),
        ("FORTIOS-300-MIB", "fnWfHTTPSURLBlocked"),
        ("FORTIOS-300-MIB", "fnWfActiveXBlocked"),
        ("FORTIOS-300-MIB", "fnWfCookieBlocked"),
        ("FORTIOS-300-MIB", "fnWfAppletBlocked"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPExamined"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPSExamined"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPAllowed"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPSAllowed"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPBlocked"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPSBlocked"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPLogged"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPSLogged"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPOverridden"),
        ("FORTIOS-300-MIB", "fnFgWfHTTPSOverridden"))
)
if mibBuilder.loadTexts:
    fnWebFilterComplianceGroup.setStatus("current")

fnFirewallComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 15)
)
fnFirewallComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnFwPolicyPktCount"),
        ("FORTIOS-300-MIB", "fnFwPolicyByteCount"))
)
if mibBuilder.loadTexts:
    fnFirewallComplianceGroup.setStatus("current")

fnApplicationComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 16)
)
fnApplicationComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnApHTTPUpTime"),
        ("FORTIOS-300-MIB", "fnApHTTPMemUsage"),
        ("FORTIOS-300-MIB", "fnApHTTPReqProcessed"),
        ("FORTIOS-300-MIB", "fnApSMTPUpTime"),
        ("FORTIOS-300-MIB", "fnApSMTPMemUsage"),
        ("FORTIOS-300-MIB", "fnApSMTPReqProcessed"),
        ("FORTIOS-300-MIB", "fnApSMTPSpamDetected"),
        ("FORTIOS-300-MIB", "fnApPOP3UpTime"),
        ("FORTIOS-300-MIB", "fnApPOP3MemUsage"),
        ("FORTIOS-300-MIB", "fnApPOP3ReqProcessed"),
        ("FORTIOS-300-MIB", "fnApPOP3SpamDetected"),
        ("FORTIOS-300-MIB", "fnApIMAPUpTime"),
        ("FORTIOS-300-MIB", "fnApIMAPMemUsage"),
        ("FORTIOS-300-MIB", "fnApIMAPReqProcessed"),
        ("FORTIOS-300-MIB", "fnApIMAPSpamDetected"),
        ("FORTIOS-300-MIB", "fnApNNTPUpTime"),
        ("FORTIOS-300-MIB", "fnApNNTPMemUsage"),
        ("FORTIOS-300-MIB", "fnApNNTPReqProcessed"),
        ("FORTIOS-300-MIB", "fnApIMUpTime"),
        ("FORTIOS-300-MIB", "fnApIMMemUsage"),
        ("FORTIOS-300-MIB", "fnApIMReqProcessed"),
        ("FORTIOS-300-MIB", "fnApSIPUpTime"),
        ("FORTIOS-300-MIB", "fnApSIPMemUsage"),
        ("FORTIOS-300-MIB", "fnApSIPClientReg"),
        ("FORTIOS-300-MIB", "fnApSIPCallHandling"),
        ("FORTIOS-300-MIB", "fnApSIPServices"),
        ("FORTIOS-300-MIB", "fnApSIPOtherReq"),
        ("FORTIOS-300-MIB", "fnAppSuNumber"),
        ("FORTIOS-300-MIB", "fnAppSuFileScanned"),
        ("FORTIOS-300-MIB", "fnAppVoIPConn"),
        ("FORTIOS-300-MIB", "fnAppVoIPCallBlocked"),
        ("FORTIOS-300-MIB", "fnAppP2PConnBlocked"),
        ("FORTIOS-300-MIB", "fnAppP2PProtEntBytes"),
        ("FORTIOS-300-MIB", "fnAppP2PProtoEntLastReset"),
        ("FORTIOS-300-MIB", "fnAppIMMessages"),
        ("FORTIOS-300-MIB", "fnAppIMFileTransfered"),
        ("FORTIOS-300-MIB", "fnAppIMFileTxBlocked"),
        ("FORTIOS-300-MIB", "fnAppIMConnBlocked"),
        ("FORTIOS-300-MIB", "fnApFTPUpTime"),
        ("FORTIOS-300-MIB", "fnApFTPMemUsage"),
        ("FORTIOS-300-MIB", "fnApFTPReqProcessed"))
)
if mibBuilder.loadTexts:
    fnApplicationComplianceGroup.setStatus("current")


# Notification objects

fnFMTrapIfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 100)
)
fnFMTrapIfChange.setObjects(
      *(("FORTIOS-300-MIB", "fnManSysSerial"),
        ("FORTIOS-300-MIB", "fnManIfName"),
        ("FORTIOS-300-MIB", "fnManIfIp"),
        ("FORTIOS-300-MIB", "fnManIfMask"))
)
if mibBuilder.loadTexts:
    fnFMTrapIfChange.setStatus(
        "current"
    )

fnTrapCpuHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 101)
)
fnTrapCpuHigh.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapCpuHigh.setStatus(
        "current"
    )

fnTrapMemLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 102)
)
fnTrapMemLow.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapMemLow.setStatus(
        "current"
    )

fnTrapLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 103)
)
fnTrapLogFull.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapLogFull.setStatus(
        "current"
    )

fnTrapTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 104)
)
fnTrapTempHigh.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapTempHigh.setStatus(
        "current"
    )

fnTrapVoltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 105)
)
fnTrapVoltageOutOfRange.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapVoltageOutOfRange.setStatus(
        "current"
    )

fnTrapPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 106)
)
fnTrapPowerSupplyFailure.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapPowerSupplyFailure.setStatus(
        "current"
    )

fnFMTrapConfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 150)
)
fnFMTrapConfChange.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnFMTrapConfChange.setStatus(
        "current"
    )

fnTrapIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 201)
)
fnTrapIpChange.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    fnTrapIpChange.setStatus(
        "current"
    )

fnFMTrapDeployComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 202)
)
fnFMTrapDeployComplete.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnFMTrapDeployComplete.setStatus(
        "current"
    )

fnFMTrapDeployInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 203)
)
fnFMTrapDeployInProgress.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnFMTrapDeployInProgress.setStatus(
        "current"
    )

fnTrapVpnTunUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 301)
)
fnTrapVpnTunUp.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTIOS-300-MIB", "fnVpnTrapLocalGateway"),
        ("FORTIOS-300-MIB", "fnVpnTrapRemoteGateway"))
)
if mibBuilder.loadTexts:
    fnTrapVpnTunUp.setStatus(
        "current"
    )

fnTrapVpnTunDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 302)
)
fnTrapVpnTunDown.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTIOS-300-MIB", "fnVpnTrapLocalGateway"),
        ("FORTIOS-300-MIB", "fnVpnTrapRemoteGateway"))
)
if mibBuilder.loadTexts:
    fnTrapVpnTunDown.setStatus(
        "current"
    )

fnTrapHaSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 401)
)
fnTrapHaSwitch.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapHaSwitch.setStatus(
        "current"
    )

fnTrapHaStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 402)
)
fnTrapHaStateChange.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapHaStateChange.setStatus(
        "obsolete"
    )

fnTrapHaHBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 403)
)
fnTrapHaHBFail.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapHaHBFail.setStatus(
        "current"
    )

fnTrapHaMemberDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 404)
)
fnTrapHaMemberDown.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapHaMemberDown.setStatus(
        "current"
    )

fnTrapHaMemberUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 405)
)
fnTrapHaMemberUp.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapHaMemberUp.setStatus(
        "current"
    )

fnTrapIdsSynFlood = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 501)
)
fnTrapIdsSynFlood.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapIdsSynFlood.setStatus(
        "obsolete"
    )

fnTrapIdsPortScan = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 502)
)
fnTrapIdsPortScan.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapIdsPortScan.setStatus(
        "obsolete"
    )

fnTrapIpsSignature = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 503)
)
fnTrapIpsSignature.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTIOS-300-MIB", "fnIpsTrapSigId"),
        ("FORTIOS-300-MIB", "fnIpsTrapSrcIp"))
)
if mibBuilder.loadTexts:
    fnTrapIpsSignature.setStatus(
        "current"
    )

fnTrapIpsAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 504)
)
fnTrapIpsAnomaly.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTIOS-300-MIB", "fnIpsTrapSigId"),
        ("FORTIOS-300-MIB", "fnIpsTrapSrcIp"))
)
if mibBuilder.loadTexts:
    fnTrapIpsAnomaly.setStatus(
        "current"
    )

fnTrapIpsPkgUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 505)
)
fnTrapIpsPkgUpdate.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapIpsPkgUpdate.setStatus(
        "current"
    )

fnTrapAvVirus = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 601)
)
fnTrapAvVirus.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTIOS-300-MIB", "fnAvTrapVirName"))
)
if mibBuilder.loadTexts:
    fnTrapAvVirus.setStatus(
        "current"
    )

fnTrapAvOversize = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 602)
)
fnTrapAvOversize.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAvOversize.setStatus(
        "current"
    )

fnTrapAvPattern = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 603)
)
fnTrapAvPattern.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAvPattern.setStatus(
        "current"
    )

fnTrapAvFragmented = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 604)
)
fnTrapAvFragmented.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAvFragmented.setStatus(
        "current"
    )

fnTrapAvEnterConserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 605)
)
fnTrapAvEnterConserve.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAvEnterConserve.setStatus(
        "current"
    )

fnTrapAvBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 606)
)
fnTrapAvBypass.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAvBypass.setStatus(
        "current"
    )

fnTrapAvOversizePass = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 607)
)
fnTrapAvOversizePass.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAvOversizePass.setStatus(
        "current"
    )

fnTrapAvOversizeBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 608)
)
fnTrapAvOversizeBlock.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapAvOversizeBlock.setStatus(
        "current"
    )

fnTrapBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 701)
)
fnTrapBridge.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapBridge.setStatus(
        "current"
    )

fnTrapImTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 801)
)
fnTrapImTableFull.setObjects(
    ("FORTIOS-300-MIB", "fnSysSerial")
)
if mibBuilder.loadTexts:
    fnTrapImTableFull.setStatus(
        "current"
    )

fnTrapFlgEventCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 901)
)
fnTrapFlgEventCount.setObjects(
    ("FORTIOS-300-MIB", "fnGenTrapMsg")
)
if mibBuilder.loadTexts:
    fnTrapFlgEventCount.setStatus(
        "current"
    )

fnTrapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 0, 999)
)
fnTrapTest.setObjects(
      *(("FORTIOS-300-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fnTrapTest.setStatus(
        "current"
    )


# Notifications groups

fnTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 6)
)
fnTrapsComplianceGroup.setObjects(
      *(("FORTIOS-300-MIB", "fnTrapCpuHigh"),
        ("FORTIOS-300-MIB", "fnTrapMemLow"),
        ("FORTIOS-300-MIB", "fnTrapLogFull"),
        ("FORTIOS-300-MIB", "fnTrapTempHigh"),
        ("FORTIOS-300-MIB", "fnTrapVoltageOutOfRange"),
        ("FORTIOS-300-MIB", "fnTrapPowerSupplyFailure"),
        ("FORTIOS-300-MIB", "fnTrapIpChange"),
        ("FORTIOS-300-MIB", "fnFMTrapDeployComplete"),
        ("FORTIOS-300-MIB", "fnFMTrapDeployInProgress"),
        ("FORTIOS-300-MIB", "fnTrapVpnTunUp"),
        ("FORTIOS-300-MIB", "fnTrapVpnTunDown"),
        ("FORTIOS-300-MIB", "fnTrapHaSwitch"),
        ("FORTIOS-300-MIB", "fnTrapHaHBFail"),
        ("FORTIOS-300-MIB", "fnTrapHaMemberDown"),
        ("FORTIOS-300-MIB", "fnTrapHaMemberUp"),
        ("FORTIOS-300-MIB", "fnTrapIpsSignature"),
        ("FORTIOS-300-MIB", "fnTrapIpsAnomaly"),
        ("FORTIOS-300-MIB", "fnTrapIpsPkgUpdate"),
        ("FORTIOS-300-MIB", "fnTrapAvVirus"),
        ("FORTIOS-300-MIB", "fnTrapAvOversize"),
        ("FORTIOS-300-MIB", "fnTrapAvPattern"),
        ("FORTIOS-300-MIB", "fnTrapAvFragmented"),
        ("FORTIOS-300-MIB", "fnTrapAvEnterConserve"),
        ("FORTIOS-300-MIB", "fnTrapAvBypass"),
        ("FORTIOS-300-MIB", "fnTrapAvOversizePass"),
        ("FORTIOS-300-MIB", "fnTrapAvOversizeBlock"),
        ("FORTIOS-300-MIB", "fnTrapImTableFull"),
        ("FORTIOS-300-MIB", "fnTrapFlgEventCount"),
        ("FORTIOS-300-MIB", "fnTrapBridge"),
        ("FORTIOS-300-MIB", "fnFMTrapConfChange"),
        ("FORTIOS-300-MIB", "fnFMTrapIfChange"),
        ("FORTIOS-300-MIB", "fnTrapTest"))
)
if mibBuilder.loadTexts:
    fnTrapsComplianceGroup.setStatus(
        "current"
    )

fnTrapsComplianceGroupOld = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 99, 7)
)
fnTrapsComplianceGroupOld.setObjects(
      *(("FORTIOS-300-MIB", "fnTrapHaStateChange"),
        ("FORTIOS-300-MIB", "fnTrapIdsSynFlood"),
        ("FORTIOS-300-MIB", "fnTrapIdsPortScan"))
)
if mibBuilder.loadTexts:
    fnTrapsComplianceGroupOld.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

fnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 99, 100)
)
fnMIBCompliance.setObjects(
      *(("FORTIOS-300-MIB", "fnSystemComplianceGroup"),
        ("FORTIOS-300-MIB", "fnHaComplianceGroup"),
        ("FORTIOS-300-MIB", "fnAuthComplianceGroup"),
        ("FORTIOS-300-MIB", "fnSessionComplianceGroup"),
        ("FORTIOS-300-MIB", "fnFirewallComplianceGroup"),
        ("FORTIOS-300-MIB", "fnVPNComplianceGroup"),
        ("FORTIOS-300-MIB", "fnHwSensorsComplianceGroup"),
        ("FORTIOS-300-MIB", "fnAntivirusComplianceGroup"),
        ("FORTIOS-300-MIB", "fnWebFilterComplianceGroup"),
        ("FORTIOS-300-MIB", "fnIpsComplianceGroup"),
        ("FORTIOS-300-MIB", "fnApplicationComplianceGroup"),
        ("FORTIOS-300-MIB", "fnManagementComplianceGroup"),
        ("FORTIOS-300-MIB", "fnTrapsComplianceGroup"),
        ("FORTIOS-300-MIB", "fnNotificationObjectsComplianceGroup"))
)
if mibBuilder.loadTexts:
    fnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTIOS-300-MIB",
    **{"FnBoolState": FnBoolState,
       "FnIndex": FnIndex,
       "FnVdIndex": FnVdIndex,
       "FnOpMode": FnOpMode,
       "FnHaMode": FnHaMode,
       "FnHaLBSchedule": FnHaLBSchedule,
       "FnAdminPermLevel": FnAdminPermLevel,
       "FnUserAuthType": FnUserAuthType,
       "FnLanguage": FnLanguage,
       "FnSessProto": FnSessProto,
       "FnModel": FnModel,
       "FnP2PProto": FnP2PProto,
       "fortinet": fortinet,
       "fnTraps": fnTraps,
       "fnTrapObjects": fnTrapObjects,
       "fnGenTrapMsg": fnGenTrapMsg,
       "fnFMTrapIfChange": fnFMTrapIfChange,
       "fnTrapCpuHigh": fnTrapCpuHigh,
       "fnTrapMemLow": fnTrapMemLow,
       "fnTrapLogFull": fnTrapLogFull,
       "fnTrapTempHigh": fnTrapTempHigh,
       "fnTrapVoltageOutOfRange": fnTrapVoltageOutOfRange,
       "fnTrapPowerSupplyFailure": fnTrapPowerSupplyFailure,
       "fnFMTrapConfChange": fnFMTrapConfChange,
       "fnTrapIpChange": fnTrapIpChange,
       "fnFMTrapDeployComplete": fnFMTrapDeployComplete,
       "fnFMTrapDeployInProgress": fnFMTrapDeployInProgress,
       "fnTrapVpnTunUp": fnTrapVpnTunUp,
       "fnTrapVpnTunDown": fnTrapVpnTunDown,
       "fnTrapHaSwitch": fnTrapHaSwitch,
       "fnTrapHaStateChange": fnTrapHaStateChange,
       "fnTrapHaHBFail": fnTrapHaHBFail,
       "fnTrapHaMemberDown": fnTrapHaMemberDown,
       "fnTrapHaMemberUp": fnTrapHaMemberUp,
       "fnTrapIdsSynFlood": fnTrapIdsSynFlood,
       "fnTrapIdsPortScan": fnTrapIdsPortScan,
       "fnTrapIpsSignature": fnTrapIpsSignature,
       "fnTrapIpsAnomaly": fnTrapIpsAnomaly,
       "fnTrapIpsPkgUpdate": fnTrapIpsPkgUpdate,
       "fnTrapAvVirus": fnTrapAvVirus,
       "fnTrapAvOversize": fnTrapAvOversize,
       "fnTrapAvPattern": fnTrapAvPattern,
       "fnTrapAvFragmented": fnTrapAvFragmented,
       "fnTrapAvEnterConserve": fnTrapAvEnterConserve,
       "fnTrapAvBypass": fnTrapAvBypass,
       "fnTrapAvOversizePass": fnTrapAvOversizePass,
       "fnTrapAvOversizeBlock": fnTrapAvOversizeBlock,
       "fnTrapBridge": fnTrapBridge,
       "fnTrapImTableFull": fnTrapImTableFull,
       "fnTrapFlgEventCount": fnTrapFlgEventCount,
       "fnTrapTest": fnTrapTest,
       "fnSystem": fnSystem,
       "fnSysModel": fnSysModel,
       "fnSysSerial": fnSysSerial,
       "fnSysVersion": fnSysVersion,
       "fnSysVersionAv": fnSysVersionAv,
       "fnSysVersionNids": fnSysVersionNids,
       "fnSysHaMode": fnSysHaMode,
       "fnSysOpMode": fnSysOpMode,
       "fnSysCpuUsage": fnSysCpuUsage,
       "fnSysMemUsage": fnSysMemUsage,
       "fnSysSesCount": fnSysSesCount,
       "fnSysDiskCapacity": fnSysDiskCapacity,
       "fnSysDiskUsage": fnSysDiskUsage,
       "fnSysMemCapacity": fnSysMemCapacity,
       "fnHa": fnHa,
       "fnHaGroupId": fnHaGroupId,
       "fnHaPriority": fnHaPriority,
       "fnHaOverride": fnHaOverride,
       "fnHaAutoSync": fnHaAutoSync,
       "fnHaSchedule": fnHaSchedule,
       "fnHaStatsTable": fnHaStatsTable,
       "fnHaStatsEntry": fnHaStatsEntry,
       "fnHaStatsIndex": fnHaStatsIndex,
       "fnHaStatsSerial": fnHaStatsSerial,
       "fnHaStatsCpuUsage": fnHaStatsCpuUsage,
       "fnHaStatsMemUsage": fnHaStatsMemUsage,
       "fnHaStatsNetUsage": fnHaStatsNetUsage,
       "fnHaStatsSesCount": fnHaStatsSesCount,
       "fnHaStatsPktCount": fnHaStatsPktCount,
       "fnHaStatsByteCount": fnHaStatsByteCount,
       "fnHaStatsIdsCount": fnHaStatsIdsCount,
       "fnHaStatsAvCount": fnHaStatsAvCount,
       "fnHaStatsHostname": fnHaStatsHostname,
       "fnHaGroupName": fnHaGroupName,
       "fnHaTrapMemberSerial": fnHaTrapMemberSerial,
       "fnAdmin": fnAdmin,
       "fnAdminNumber": fnAdminNumber,
       "fnAdminTable": fnAdminTable,
       "fnAdminEntry": fnAdminEntry,
       "fnAdminIndex": fnAdminIndex,
       "fnAdminName": fnAdminName,
       "fnAdminAddr": fnAdminAddr,
       "fnAdminMask": fnAdminMask,
       "fnAdminVdom": fnAdminVdom,
       "fnUsers": fnUsers,
       "fnUserNumber": fnUserNumber,
       "fnUserTable": fnUserTable,
       "fnUserEntry": fnUserEntry,
       "fnUserIndex": fnUserIndex,
       "fnUserName": fnUserName,
       "fnUserAuth": fnUserAuth,
       "fnUserState": fnUserState,
       "fnUserVdom": fnUserVdom,
       "fnOptions": fnOptions,
       "fnOptIdleTimeout": fnOptIdleTimeout,
       "fnOptAuthTimeout": fnOptAuthTimeout,
       "fnOptLanguage": fnOptLanguage,
       "fnOptLcdProtection": fnOptLcdProtection,
       "fnHwSensors": fnHwSensors,
       "fnHwSensorCount": fnHwSensorCount,
       "fnHwSensorTable": fnHwSensorTable,
       "fnHwSensorEntry": fnHwSensorEntry,
       "fnHwSensorEntIndex": fnHwSensorEntIndex,
       "fnHwSensorEntName": fnHwSensorEntName,
       "fnHwSensorEntValue": fnHwSensorEntValue,
       "fnHwSensorEntAlarmStatus": fnHwSensorEntAlarmStatus,
       "fnDomains": fnDomains,
       "fnVdNumber": fnVdNumber,
       "fnVdTable": fnVdTable,
       "fnVdEntry": fnVdEntry,
       "fnVdEntIndex": fnVdEntIndex,
       "fnVdEntName": fnVdEntName,
       "fnVdEntOpMode": fnVdEntOpMode,
       "fnVdMaxVdoms": fnVdMaxVdoms,
       "fnVdEnabled": fnVdEnabled,
       "fnIntf": fnIntf,
       "fnIntfTable": fnIntfTable,
       "fnIntfEntry": fnIntfEntry,
       "fnIntfEntVdom": fnIntfEntVdom,
       "fnIp": fnIp,
       "fnIpSessTable": fnIpSessTable,
       "fnIpSessEntry": fnIpSessEntry,
       "fnIpSessIndex": fnIpSessIndex,
       "fnIpSessProto": fnIpSessProto,
       "fnIpSessFromAddr": fnIpSessFromAddr,
       "fnIpSessFromPort": fnIpSessFromPort,
       "fnIpSessToAddr": fnIpSessToAddr,
       "fnIpSessToPort": fnIpSessToPort,
       "fnIpSessExp": fnIpSessExp,
       "fnIpSessVdom": fnIpSessVdom,
       "fnIpSessStatsTable": fnIpSessStatsTable,
       "fnIpSessStatsEntry": fnIpSessStatsEntry,
       "fnIpSessStatsVdomIndex": fnIpSessStatsVdomIndex,
       "fnIpSessNumber": fnIpSessNumber,
       "fnFirewall": fnFirewall,
       "fnFwPolicyStatsTable": fnFwPolicyStatsTable,
       "fnFwPolicyStatsEntry": fnFwPolicyStatsEntry,
       "fnFwPolicyStatsVdomIndex": fnFwPolicyStatsVdomIndex,
       "fnFwPolicyID": fnFwPolicyID,
       "fnFwPolicyPktCount": fnFwPolicyPktCount,
       "fnFwPolicyByteCount": fnFwPolicyByteCount,
       "fnVpn": fnVpn,
       "fnVpnDialupTable": fnVpnDialupTable,
       "fnVpnDialupEntry": fnVpnDialupEntry,
       "fnVpnDialupIndex": fnVpnDialupIndex,
       "fnVpnDialupGateway": fnVpnDialupGateway,
       "fnVpnDialupLifetime": fnVpnDialupLifetime,
       "fnVpnDialupTimeout": fnVpnDialupTimeout,
       "fnVpnDialupSrcBegin": fnVpnDialupSrcBegin,
       "fnVpnDialupSrcEnd": fnVpnDialupSrcEnd,
       "fnVpnDialupDstAddr": fnVpnDialupDstAddr,
       "fnVpnDialupVdom": fnVpnDialupVdom,
       "fnVpnDialupInOctets": fnVpnDialupInOctets,
       "fnVpnDialupOutOctets": fnVpnDialupOutOctets,
       "fnVpnTrapLocalGateway": fnVpnTrapLocalGateway,
       "fnVpnTrapRemoteGateway": fnVpnTrapRemoteGateway,
       "fnVpnTunTable": fnVpnTunTable,
       "fnVpnTunEntry": fnVpnTunEntry,
       "fnVpnTunEntIndex": fnVpnTunEntIndex,
       "fnVpnTunEntPhase1Name": fnVpnTunEntPhase1Name,
       "fnVpnTunEntPhase2Name": fnVpnTunEntPhase2Name,
       "fnVpnTunEntRemGwyIp": fnVpnTunEntRemGwyIp,
       "fnVpnTunEntRemGwyPort": fnVpnTunEntRemGwyPort,
       "fnVpnTunEntLocGwyIp": fnVpnTunEntLocGwyIp,
       "fnVpnTunEntLocGwyPort": fnVpnTunEntLocGwyPort,
       "fnVpnTunEntSelectorSrcBeginIp": fnVpnTunEntSelectorSrcBeginIp,
       "fnVpnTunEntSelectorSrcEndIp": fnVpnTunEntSelectorSrcEndIp,
       "fnVpnTunEntSelectorSrcPort": fnVpnTunEntSelectorSrcPort,
       "fnVpnTunEntSelectorDstBeginIp": fnVpnTunEntSelectorDstBeginIp,
       "fnVpnTunEntSelectorDstEndIp": fnVpnTunEntSelectorDstEndIp,
       "fnVpnTunEntSelectorDstPort": fnVpnTunEntSelectorDstPort,
       "fnVpnTunEntSelectorProto": fnVpnTunEntSelectorProto,
       "fnVpnTunEntLifeSecs": fnVpnTunEntLifeSecs,
       "fnVpnTunEntLifeBytes": fnVpnTunEntLifeBytes,
       "fnVpnTunEntTimeout": fnVpnTunEntTimeout,
       "fnVpnTunEntInOctets": fnVpnTunEntInOctets,
       "fnVpnTunEntOutOctets": fnVpnTunEntOutOctets,
       "fnVpnTunEntStatus": fnVpnTunEntStatus,
       "fnVpnTunEntVdom": fnVpnTunEntVdom,
       "fnVpnSslStatsTable": fnVpnSslStatsTable,
       "fnVpnSslStatsEntry": fnVpnSslStatsEntry,
       "fnVpnSslStatsVdomIndex": fnVpnSslStatsVdomIndex,
       "fnVpnSslState": fnVpnSslState,
       "fnVpnSslStatsLoginUsers": fnVpnSslStatsLoginUsers,
       "fnVpnSslStatsMaxUsers": fnVpnSslStatsMaxUsers,
       "fnVpnSslStatsActiveWebSessions": fnVpnSslStatsActiveWebSessions,
       "fnVpnSslStatsMaxWebSessions": fnVpnSslStatsMaxWebSessions,
       "fnVpnSslStatsActiveTunnels": fnVpnSslStatsActiveTunnels,
       "fnVpnSslStatsMaxTunnels": fnVpnSslStatsMaxTunnels,
       "fnVpnSslTunnelTable": fnVpnSslTunnelTable,
       "fnVpnSslTunnelEntry": fnVpnSslTunnelEntry,
       "fnVpnSslTunnelIndex": fnVpnSslTunnelIndex,
       "fnVpnSslTunnelVdom": fnVpnSslTunnelVdom,
       "fnVpnSslTunnelUserName": fnVpnSslTunnelUserName,
       "fnVpnSslTunnelSrcIp": fnVpnSslTunnelSrcIp,
       "fnVpnSslTunnelIp": fnVpnSslTunnelIp,
       "fnVpnSslTunnelUpTime": fnVpnSslTunnelUpTime,
       "fnVpnSslTunnelBytesIn": fnVpnSslTunnelBytesIn,
       "fnVpnSslTunnelBytesOut": fnVpnSslTunnelBytesOut,
       "fnManagement": fnManagement,
       "fnManSysSerial": fnManSysSerial,
       "fnManIfName": fnManIfName,
       "fnManIfIp": fnManIfIp,
       "fnManIfMask": fnManIfMask,
       "fnAntivirus": fnAntivirus,
       "fnAvTrapVirName": fnAvTrapVirName,
       "fnAvStatsTable": fnAvStatsTable,
       "fnAvStatsEntry": fnAvStatsEntry,
       "fnAvStatsVdomIndex": fnAvStatsVdomIndex,
       "fnAvVirusDetected": fnAvVirusDetected,
       "fnAvVirusBlocked": fnAvVirusBlocked,
       "fnAvHTTPVirusDetected": fnAvHTTPVirusDetected,
       "fnAvHTTPVirusBlocked": fnAvHTTPVirusBlocked,
       "fnAvSMTPVirusDetected": fnAvSMTPVirusDetected,
       "fnAvSMTPVirusBlocked": fnAvSMTPVirusBlocked,
       "fnAvPOP3VirusDetected": fnAvPOP3VirusDetected,
       "fnAvPOP3VirusBlocked": fnAvPOP3VirusBlocked,
       "fnAvIMAPVirusDetected": fnAvIMAPVirusDetected,
       "fnAvIMAPVirusBlocked": fnAvIMAPVirusBlocked,
       "fnAvFTPVirusDetected": fnAvFTPVirusDetected,
       "fnAvFTPVirusBlocked": fnAvFTPVirusBlocked,
       "fnAvIMVirusDetected": fnAvIMVirusDetected,
       "fnAvIMVirusBlocked": fnAvIMVirusBlocked,
       "fnAvNNTPVirusDetected": fnAvNNTPVirusDetected,
       "fnAvNNTPVirusBlocked": fnAvNNTPVirusBlocked,
       "fnAvOversizedDetected": fnAvOversizedDetected,
       "fnAvOversizedBlocked": fnAvOversizedBlocked,
       "fnWebfilter": fnWebfilter,
       "fnWebfilterStatsTable": fnWebfilterStatsTable,
       "fnWebfilterStatsEntry": fnWebfilterStatsEntry,
       "fnWfStatsVdomIndex": fnWfStatsVdomIndex,
       "fnWfHTTPBlocked": fnWfHTTPBlocked,
       "fnWfHTTPSBlocked": fnWfHTTPSBlocked,
       "fnWfHTTPURLBlocked": fnWfHTTPURLBlocked,
       "fnWfHTTPSURLBlocked": fnWfHTTPSURLBlocked,
       "fnWfActiveXBlocked": fnWfActiveXBlocked,
       "fnWfCookieBlocked": fnWfCookieBlocked,
       "fnWfAppletBlocked": fnWfAppletBlocked,
       "fnFortiGuardStatsTable": fnFortiGuardStatsTable,
       "fnFortiGuardStatsEntry": fnFortiGuardStatsEntry,
       "fnFgWfStatsVdomIndex": fnFgWfStatsVdomIndex,
       "fnFgWfHTTPExamined": fnFgWfHTTPExamined,
       "fnFgWfHTTPSExamined": fnFgWfHTTPSExamined,
       "fnFgWfHTTPAllowed": fnFgWfHTTPAllowed,
       "fnFgWfHTTPSAllowed": fnFgWfHTTPSAllowed,
       "fnFgWfHTTPBlocked": fnFgWfHTTPBlocked,
       "fnFgWfHTTPSBlocked": fnFgWfHTTPSBlocked,
       "fnFgWfHTTPLogged": fnFgWfHTTPLogged,
       "fnFgWfHTTPSLogged": fnFgWfHTTPSLogged,
       "fnFgWfHTTPOverridden": fnFgWfHTTPOverridden,
       "fnFgWfHTTPSOverridden": fnFgWfHTTPSOverridden,
       "fnIps": fnIps,
       "fnIpsTrapSigId": fnIpsTrapSigId,
       "fnIpsTrapSrcIp": fnIpsTrapSrcIp,
       "fnIpsTrapSigMsg": fnIpsTrapSigMsg,
       "fnIpsStatsTable": fnIpsStatsTable,
       "fnIpsStatsEntry": fnIpsStatsEntry,
       "fnIpsStatsVdomIndex": fnIpsStatsVdomIndex,
       "fnIpsIntrusionsDetected": fnIpsIntrusionsDetected,
       "fnIpsIntrusionsBlocked": fnIpsIntrusionsBlocked,
       "fnIpsCritSevDetections": fnIpsCritSevDetections,
       "fnIpsHighSevDetections": fnIpsHighSevDetections,
       "fnIpsMedSevDetections": fnIpsMedSevDetections,
       "fnIpsLowSevDetections": fnIpsLowSevDetections,
       "fnIpsInfoSevDetections": fnIpsInfoSevDetections,
       "fnIpsSignatureDetections": fnIpsSignatureDetections,
       "fnIpsAnomalyDetections": fnIpsAnomalyDetections,
       "fnApplications": fnApplications,
       "fnAppProxyHTTP": fnAppProxyHTTP,
       "fnApHTTPUpTime": fnApHTTPUpTime,
       "fnApHTTPMemUsage": fnApHTTPMemUsage,
       "fnApHTTPStatsTable": fnApHTTPStatsTable,
       "fnApHTTPStatsEntry": fnApHTTPStatsEntry,
       "fnApHTTPStatsVdomIndex": fnApHTTPStatsVdomIndex,
       "fnApHTTPReqProcessed": fnApHTTPReqProcessed,
       "fnAppProxySMTP": fnAppProxySMTP,
       "fnApSMTPUpTime": fnApSMTPUpTime,
       "fnApSMTPMemUsage": fnApSMTPMemUsage,
       "fnApSMTPStatsTable": fnApSMTPStatsTable,
       "fnApSMTPStatsEntry": fnApSMTPStatsEntry,
       "fnApSMTPStatsVdomIndex": fnApSMTPStatsVdomIndex,
       "fnApSMTPReqProcessed": fnApSMTPReqProcessed,
       "fnApSMTPSpamDetected": fnApSMTPSpamDetected,
       "fnAppProxyPOP3": fnAppProxyPOP3,
       "fnApPOP3UpTime": fnApPOP3UpTime,
       "fnApPOP3MemUsage": fnApPOP3MemUsage,
       "fnApPOP3StatsTable": fnApPOP3StatsTable,
       "fnApPOP3StatsEntry": fnApPOP3StatsEntry,
       "fnApPOP3StatsVdomIndex": fnApPOP3StatsVdomIndex,
       "fnApPOP3ReqProcessed": fnApPOP3ReqProcessed,
       "fnApPOP3SpamDetected": fnApPOP3SpamDetected,
       "fnAppProxyIMAP": fnAppProxyIMAP,
       "fnApIMAPUpTime": fnApIMAPUpTime,
       "fnApIMAPMemUsage": fnApIMAPMemUsage,
       "fnApIMAPStatsTable": fnApIMAPStatsTable,
       "fnApIMAPStatsEntry": fnApIMAPStatsEntry,
       "fnApIMAPStatsVdomIndex": fnApIMAPStatsVdomIndex,
       "fnApIMAPReqProcessed": fnApIMAPReqProcessed,
       "fnApIMAPSpamDetected": fnApIMAPSpamDetected,
       "fnAppProxyNNTP": fnAppProxyNNTP,
       "fnApNNTPUpTime": fnApNNTPUpTime,
       "fnApNNTPMemUsage": fnApNNTPMemUsage,
       "fnApNNTPStatsTable": fnApNNTPStatsTable,
       "fnApNNTPStatsEntry": fnApNNTPStatsEntry,
       "fnApNNTPStatsVdomIndex": fnApNNTPStatsVdomIndex,
       "fnApNNTPReqProcessed": fnApNNTPReqProcessed,
       "fnAppProxyIM": fnAppProxyIM,
       "fnApIMUpTime": fnApIMUpTime,
       "fnApIMMemUsage": fnApIMMemUsage,
       "fnApIMStatsTable": fnApIMStatsTable,
       "fnApIMStatsEntry": fnApIMStatsEntry,
       "fnApIMStatsVdomIndex": fnApIMStatsVdomIndex,
       "fnApIMReqProcessed": fnApIMReqProcessed,
       "fnAppProxySIP": fnAppProxySIP,
       "fnApSIPUpTime": fnApSIPUpTime,
       "fnApSIPMemUsage": fnApSIPMemUsage,
       "fnApSIPStatsTable": fnApSIPStatsTable,
       "fnApSIPStatsEntry": fnApSIPStatsEntry,
       "fnApSIPStatsVdomIndex": fnApSIPStatsVdomIndex,
       "fnApSIPClientReg": fnApSIPClientReg,
       "fnApSIPCallHandling": fnApSIPCallHandling,
       "fnApSIPServices": fnApSIPServices,
       "fnApSIPOtherReq": fnApSIPOtherReq,
       "fnAppScanUnit": fnAppScanUnit,
       "fnAppSuNumber": fnAppSuNumber,
       "fnAppSuStatsTable": fnAppSuStatsTable,
       "fnAppSuStatsEntry": fnAppSuStatsEntry,
       "fnAppSuIndex": fnAppSuIndex,
       "fnAppSuFileScanned": fnAppSuFileScanned,
       "fnAppVoIP": fnAppVoIP,
       "fnAppVoIPStatsTable": fnAppVoIPStatsTable,
       "fnAppVoIPStatsEntry": fnAppVoIPStatsEntry,
       "fnAppVoIPStatsVdomIndex": fnAppVoIPStatsVdomIndex,
       "fnAppVoIPConn": fnAppVoIPConn,
       "fnAppVoIPCallBlocked": fnAppVoIPCallBlocked,
       "fnAppP2P": fnAppP2P,
       "fnAppP2PStatsTable": fnAppP2PStatsTable,
       "fnAppP2PStatsEntry": fnAppP2PStatsEntry,
       "fnAppP2PStatsVdomIndex": fnAppP2PStatsVdomIndex,
       "fnAppP2PConnBlocked": fnAppP2PConnBlocked,
       "fnAppP2PProtoTable": fnAppP2PProtoTable,
       "fnAppP2PProtoEntry": fnAppP2PProtoEntry,
       "fnAppP2PProtEntVdIndex": fnAppP2PProtEntVdIndex,
       "fnAppP2PProtEntProto": fnAppP2PProtEntProto,
       "fnAppP2PProtEntBytes": fnAppP2PProtEntBytes,
       "fnAppP2PProtoEntLastReset": fnAppP2PProtoEntLastReset,
       "fnAppIM": fnAppIM,
       "fnAppIMStatsTable": fnAppIMStatsTable,
       "fnAppIMStatsEntry": fnAppIMStatsEntry,
       "fnAppIMStatsVdomIndex": fnAppIMStatsVdomIndex,
       "fnAppIMMessages": fnAppIMMessages,
       "fnAppIMFileTransfered": fnAppIMFileTransfered,
       "fnAppIMFileTxBlocked": fnAppIMFileTxBlocked,
       "fnAppIMConnBlocked": fnAppIMConnBlocked,
       "fnAppProxyFTP": fnAppProxyFTP,
       "fnApFTPUpTime": fnApFTPUpTime,
       "fnApFTPMemUsage": fnApFTPMemUsage,
       "fnApFTPStatsTable": fnApFTPStatsTable,
       "fnApFTPStatsEntry": fnApFTPStatsEntry,
       "fnApFTPStatsVdomIndex": fnApFTPStatsVdomIndex,
       "fnApFTPReqProcessed": fnApFTPReqProcessed,
       "fnMIBConformance": fnMIBConformance,
       "fnSystemComplianceGroup": fnSystemComplianceGroup,
       "fnHaComplianceGroup": fnHaComplianceGroup,
       "fnAuthComplianceGroup": fnAuthComplianceGroup,
       "fnSessionComplianceGroup": fnSessionComplianceGroup,
       "fnVPNComplianceGroup": fnVPNComplianceGroup,
       "fnTrapsComplianceGroup": fnTrapsComplianceGroup,
       "fnTrapsComplianceGroupOld": fnTrapsComplianceGroupOld,
       "fnManagementComplianceGroup": fnManagementComplianceGroup,
       "fnHwSensorsComplianceGroup": fnHwSensorsComplianceGroup,
       "fnNotificationObjectsComplianceGroup": fnNotificationObjectsComplianceGroup,
       "fnAntivirusComplianceGroup": fnAntivirusComplianceGroup,
       "fnIpsComplianceGroup": fnIpsComplianceGroup,
       "fnWebFilterComplianceGroup": fnWebFilterComplianceGroup,
       "fnFirewallComplianceGroup": fnFirewallComplianceGroup,
       "fnApplicationComplianceGroup": fnApplicationComplianceGroup,
       "fnMIBCompliance": fnMIBCompliance}
)

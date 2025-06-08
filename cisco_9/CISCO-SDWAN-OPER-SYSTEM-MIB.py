# SNMP MIB module (CISCO-SDWAN-OPER-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SDWAN-OPER-SYSTEM-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:52:58 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSdwanOperSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004)
)
if mibBuilder.loadTexts:
    ciscoSdwanOperSystemMIB.setRevisions(
        ("2021-01-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class NotificationSeverity(TextualConvention, Integer32):
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )



class DomainId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class SiteId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class CiscoSdwanIpAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_CiscoSdwanSystemMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSdwanSystemMIBNotifs = _CiscoSdwanSystemMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 0)
)
_CiscoSdwanOperSystemMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanOperSystemMIBObjects = _CiscoSdwanOperSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1)
)
_SystemStatus_ObjectIdentity = ObjectIdentity
systemStatus = _SystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1)
)
_SystemStatusPersonality_Type = String
_SystemStatusPersonality_Object = MibScalar
systemStatusPersonality = _SystemStatusPersonality_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 1),
    _SystemStatusPersonality_Type()
)
systemStatusPersonality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusPersonality.setStatus("current")
_SystemStatusVersion_Type = String
_SystemStatusVersion_Object = MibScalar
systemStatusVersion = _SystemStatusVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 2),
    _SystemStatusVersion_Type()
)
systemStatusVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVersion.setStatus("current")
_SystemStatusDiskStatus_Type = String
_SystemStatusDiskStatus_Object = MibScalar
systemStatusDiskStatus = _SystemStatusDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 5),
    _SystemStatusDiskStatus_Type()
)
systemStatusDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskStatus.setStatus("current")
_SystemStatusRebootReason_Type = String
_SystemStatusRebootReason_Object = MibScalar
systemStatusRebootReason = _SystemStatusRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 6),
    _SystemStatusRebootReason_Type()
)
systemStatusRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusRebootReason.setStatus("current")
_SystemStatusUptime_Type = String
_SystemStatusUptime_Object = MibScalar
systemStatusUptime = _SystemStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 8),
    _SystemStatusUptime_Type()
)
systemStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusUptime.setStatus("current")
_SystemStatusMin1Avg_Type = String
_SystemStatusMin1Avg_Object = MibScalar
systemStatusMin1Avg = _SystemStatusMin1Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 9),
    _SystemStatusMin1Avg_Type()
)
systemStatusMin1Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMin1Avg.setStatus("current")
_SystemStatusMin5Avg_Type = String
_SystemStatusMin5Avg_Object = MibScalar
systemStatusMin5Avg = _SystemStatusMin5Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 10),
    _SystemStatusMin5Avg_Type()
)
systemStatusMin5Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMin5Avg.setStatus("current")
_SystemStatusMin15Avg_Type = String
_SystemStatusMin15Avg_Object = MibScalar
systemStatusMin15Avg = _SystemStatusMin15Avg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 11),
    _SystemStatusMin15Avg_Type()
)
systemStatusMin15Avg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMin15Avg.setStatus("current")
_SystemStatusCpuUser_Type = String
_SystemStatusCpuUser_Object = MibScalar
systemStatusCpuUser = _SystemStatusCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 14),
    _SystemStatusCpuUser_Type()
)
systemStatusCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCpuUser.setStatus("current")
_SystemStatusCpuSystem_Type = String
_SystemStatusCpuSystem_Object = MibScalar
systemStatusCpuSystem = _SystemStatusCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 15),
    _SystemStatusCpuSystem_Type()
)
systemStatusCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCpuSystem.setStatus("current")
_SystemStatusCpuIdle_Type = String
_SystemStatusCpuIdle_Object = MibScalar
systemStatusCpuIdle = _SystemStatusCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 16),
    _SystemStatusCpuIdle_Type()
)
systemStatusCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusCpuIdle.setStatus("current")
_SystemStatusMemTotal_Type = Counter64
_SystemStatusMemTotal_Object = MibScalar
systemStatusMemTotal = _SystemStatusMemTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 17),
    _SystemStatusMemTotal_Type()
)
systemStatusMemTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemTotal.setStatus("current")
_SystemStatusMemUsed_Type = Counter64
_SystemStatusMemUsed_Object = MibScalar
systemStatusMemUsed = _SystemStatusMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 18),
    _SystemStatusMemUsed_Type()
)
systemStatusMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemUsed.setStatus("current")
_SystemStatusMemFree_Type = Counter64
_SystemStatusMemFree_Object = MibScalar
systemStatusMemFree = _SystemStatusMemFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 19),
    _SystemStatusMemFree_Type()
)
systemStatusMemFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemFree.setStatus("current")
_SystemStatusMemBuffers_Type = Counter64
_SystemStatusMemBuffers_Object = MibScalar
systemStatusMemBuffers = _SystemStatusMemBuffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 20),
    _SystemStatusMemBuffers_Type()
)
systemStatusMemBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemBuffers.setStatus("current")
_SystemStatusMemCached_Type = Counter64
_SystemStatusMemCached_Object = MibScalar
systemStatusMemCached = _SystemStatusMemCached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 21),
    _SystemStatusMemCached_Type()
)
systemStatusMemCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusMemCached.setStatus("current")
_SystemStatusDiskFs_Type = String
_SystemStatusDiskFs_Object = MibScalar
systemStatusDiskFs = _SystemStatusDiskFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 22),
    _SystemStatusDiskFs_Type()
)
systemStatusDiskFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskFs.setStatus("current")
_SystemStatusDiskSize_Type = String
_SystemStatusDiskSize_Object = MibScalar
systemStatusDiskSize = _SystemStatusDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 23),
    _SystemStatusDiskSize_Type()
)
systemStatusDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskSize.setStatus("current")
_SystemStatusDiskUsed_Type = String
_SystemStatusDiskUsed_Object = MibScalar
systemStatusDiskUsed = _SystemStatusDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 24),
    _SystemStatusDiskUsed_Type()
)
systemStatusDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskUsed.setStatus("current")
_SystemStatusDiskAvail_Type = String
_SystemStatusDiskAvail_Object = MibScalar
systemStatusDiskAvail = _SystemStatusDiskAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 25),
    _SystemStatusDiskAvail_Type()
)
systemStatusDiskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskAvail.setStatus("current")
_SystemStatusDiskUse_Type = Counter64
_SystemStatusDiskUse_Object = MibScalar
systemStatusDiskUse = _SystemStatusDiskUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 26),
    _SystemStatusDiskUse_Type()
)
systemStatusDiskUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskUse.setStatus("current")
_SystemStatusDiskTotalBytes_Type = Counter64
_SystemStatusDiskTotalBytes_Object = MibScalar
systemStatusDiskTotalBytes = _SystemStatusDiskTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 27),
    _SystemStatusDiskTotalBytes_Type()
)
systemStatusDiskTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskTotalBytes.setStatus("current")
_SystemStatusDiskUsedBytes_Type = Counter64
_SystemStatusDiskUsedBytes_Object = MibScalar
systemStatusDiskUsedBytes = _SystemStatusDiskUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 28),
    _SystemStatusDiskUsedBytes_Type()
)
systemStatusDiskUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskUsedBytes.setStatus("current")
_SystemStatusDiskAvailBytes_Type = Counter64
_SystemStatusDiskAvailBytes_Object = MibScalar
systemStatusDiskAvailBytes = _SystemStatusDiskAvailBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 29),
    _SystemStatusDiskAvailBytes_Type()
)
systemStatusDiskAvailBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskAvailBytes.setStatus("current")
_SystemStatusDiskMount_Type = String
_SystemStatusDiskMount_Object = MibScalar
systemStatusDiskMount = _SystemStatusDiskMount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 30),
    _SystemStatusDiskMount_Type()
)
systemStatusDiskMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskMount.setStatus("current")
_SystemStatusServices_Type = String
_SystemStatusServices_Object = MibScalar
systemStatusServices = _SystemStatusServices_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 31),
    _SystemStatusServices_Type()
)
systemStatusServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusServices.setStatus("current")
_SystemStatusVmanaged_Type = TruthValue
_SystemStatusVmanaged_Object = MibScalar
systemStatusVmanaged = _SystemStatusVmanaged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 36),
    _SystemStatusVmanaged_Type()
)
systemStatusVmanaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusVmanaged.setStatus("current")
_SystemStatusPseudoConfirmCommit_Type = Unsigned32
_SystemStatusPseudoConfirmCommit_Object = MibScalar
systemStatusPseudoConfirmCommit = _SystemStatusPseudoConfirmCommit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 37),
    _SystemStatusPseudoConfirmCommit_Type()
)
systemStatusPseudoConfirmCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusPseudoConfirmCommit.setStatus("current")


class _SystemStatusConfigTemplateName_Type(String):
    """Custom type systemStatusConfigTemplateName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemStatusConfigTemplateName_Type.__name__ = "String"
_SystemStatusConfigTemplateName_Object = MibScalar
systemStatusConfigTemplateName = _SystemStatusConfigTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 38),
    _SystemStatusConfigTemplateName_Type()
)
systemStatusConfigTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusConfigTemplateName.setStatus("current")


class _SystemStatusModel_Type(Integer32):
    """Custom type systemStatusModel based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              54,
              55,
              56,
              57,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              84,
              85,
              86,
              87,
              100,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              212,
              213,
              214,
              215,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              288,
              289,
              290,
              291,
              292)
        )
    )
    namedValues = NamedValues(
        *(("vsmart", 1),
          ("vmanage", 2),
          ("vbond", 3),
          ("vedge-1000", 4),
          ("vedge-2000", 5),
          ("vedge-100", 6),
          ("vedge-100-W2", 7),
          ("vedge-100-WM", 8),
          ("vedge-100-M2", 9),
          ("vedge-100-M", 10),
          ("vedge-100-B", 11),
          ("vedge-cloud", 12),
          ("vcontainer", 13),
          ("vedge-5000", 14),
          ("vedge-CSR-1000v", 15),
          ("vedge-ISR-4331", 16),
          ("vedge-ISR-4321", 17),
          ("vedge-ISR-4351", 18),
          ("vedge-ISR-4221", 19),
          ("vedge-ASR-1001-X", 20),
          ("vedge-ASR-1001-HX", 21),
          ("vedge-ASR-1002-X", 22),
          ("vedge-ASR-1002-HX", 23),
          ("vedge-C1111-8PLTEEA", 24),
          ("vedge-C1111-8PLTELA", 25),
          ("vedge-C1117-4PLTEEA", 26),
          ("vedge-C1117-4PLTELA", 27),
          ("vedge-C1116-4PLTEEA", 28),
          ("vedge-C1116-4PLTELA", 29),
          ("vedge-ISRv", 30),
          ("vedge-C1111-8P", 31),
          ("vedge-C1111-4PLTEEA", 32),
          ("vedge-C1111-4PLTELA", 33),
          ("vedge-C1117-4PMLTEEA", 34),
          ("vedge-C1111-4P", 35),
          ("vedge-C1116-4P", 36),
          ("vedge-C1117-4P", 37),
          ("vedge-C1117-4PM", 38),
          ("vedge-C1101-4P", 39),
          ("vedge-C1101-4PLTEP", 40),
          ("vedge-C1111X-8P", 41),
          ("vedge-C1111-8PLTEEAW", 42),
          ("vedge-C1111-8PW", 43),
          ("vedge-ISR-4431", 44),
          ("vedge-ISR-4451-X", 45),
          ("vedge-ISR-4221X", 46),
          ("vedge-ISR-4461", 47),
          ("vedge-C8300-1N1S-6G", 48),
          ("vedge-C8300-1N1S-4G2X", 49),
          ("vedge-CE-9515", 54),
          ("vedge-CE-9511", 55),
          ("vedge-IR-1101", 56),
          ("vedge-C1121X-8PLTEPW", 57),
          ("vedge-C1161X-8P", 60),
          ("vedge-C1161X-8PLTEP", 61),
          ("vedge-C1111-8PLTEAEAW", 62),
          ("vedge-C1121-8P", 63),
          ("vedge-C1121-8PLTEP", 64),
          ("vedge-C1121X-8PLTEPWA", 65),
          ("vedge-C1127X-8PMLTEP", 66),
          ("vedge-C1109-4PLTE2P", 68),
          ("vedge-C1101-4PLTEPW", 69),
          ("vedge-C1109-4PLTE2PW", 70),
          ("vedge-C1111-8PLTELAW", 71),
          ("vedge-C1121X-8P", 72),
          ("vedge-C1121X-8PLTEP", 73),
          ("vedge-C1126X-8PLTEP", 74),
          ("vedge-C1127X-8PLTEP", 75),
          ("vedge-C8500-12X4QC", 76),
          ("vedge-C8500-12X", 77),
          ("vedge-C1121-8PLTEPW", 78),
          ("vedge-C1113-8PMLTEEA", 79),
          ("vedge-ISR1100-4G", 80),
          ("vedge-ISR1100-4GLTE", 81),
          ("vedge-ISR1100-6G", 82),
          ("vedge-C8300-2N2S-6G", 84),
          ("vedge-C8300-2N2S-4G2X", 85),
          ("vedge-C8500L-8G4X", 86),
          ("vedge-C8500L-8S4X", 87),
          ("vedge-sim", 100),
          ("vedge-NFVIS-ENCS5100", 200),
          ("vedge-NFVIS-ENCS5400", 201),
          ("vedge-NFVIS-UCSC-M5", 202),
          ("vedge-NFVIS-UCSC-E", 203),
          ("vedge-NFVIS-CSP2100", 204),
          ("vedge-NFVIS-CSP2100-X1", 205),
          ("vedge-NFVIS-CSP2100-X2", 206),
          ("vedge-NFVIS-CSP2100-CSP-5444", 207),
          ("vedge-C1161-8P", 212),
          ("vedge-C1161-8PLTEP", 213),
          ("vedge-C1126-8PLTEP", 214),
          ("vedge-C1127-8PLTEP", 215),
          ("vedge-C1127-8PMLTEP", 216),
          ("vedge-C1121-4P", 217),
          ("vedge-C1121-4PLTEP", 218),
          ("vedge-C1128-8PLTEP", 219),
          ("vedge-C1111-4PW", 220),
          ("vedge-C1112-8P", 221),
          ("vedge-C1112-8PLTEEA", 222),
          ("vedge-C1112-8PLTEEAW", 223),
          ("vedge-C1112-8PW", 224),
          ("vedge-C1113-8P", 225),
          ("vedge-C1113-8PLTEEA", 226),
          ("vedge-C1113-8PLTEEAW", 227),
          ("vedge-C1113-8PLTELAW", 228),
          ("vedge-C1113-8PLTELA", 229),
          ("vedge-C1113-8PM", 230),
          ("vedge-C1113-8PMW", 231),
          ("vedge-C1113-8PW", 232),
          ("vedge-C1116-4PLTEEAW", 233),
          ("vedge-C1116-4PW", 234),
          ("vedge-C1117-4PLTEEAW", 235),
          ("vedge-C1117-4PMLTEEAW", 236),
          ("vedge-C1117-4PMW", 237),
          ("vedge-C1117-4PW", 238),
          ("vedge-C1118-8P", 239),
          ("vedge-C1109-2PLTEGB", 240),
          ("vedge-C1109-2PLTEUS", 241),
          ("vedge-C1109-2PLTEVZ", 242),
          ("vedge-C1113-8PLTEW", 243),
          ("vedge-C1112-8PLTEEAWE", 244),
          ("vedge-C1112-8PWE", 245),
          ("vedge-C1113-8PLTELAWZ", 246),
          ("vedge-C1113-8PMWE", 247),
          ("vedge-C1116-4PLTEEAWE", 248),
          ("vedge-C1116-4PWE", 249),
          ("vedge-C1117-4PMLTEEAWE", 251),
          ("vedge-C1117-4PMWE", 252),
          ("vedge-C8200-1N-4G", 253),
          ("vedge-ISR1100-4GLTENA-XE", 254),
          ("vedge-ISR1100-4G-XE", 255),
          ("vedge-ISR1100-6G-XE", 256),
          ("vedge-NFVIS-C8200-UCPE", 257),
          ("vedge-C8300-1N1S-6T", 258),
          ("vedge-C8300-1N1S-4T2X", 259),
          ("vedge-C8300-2N2S-6T", 260),
          ("vedge-C8300-2N2S-4T2X", 261),
          ("vedge-C8200-1N-4T", 262),
          ("vedge-ESR-6300", 263),
          ("vedge-C8000V", 264),
          ("vedge-ISR1100X-4G", 265),
          ("vedge-ISR1100X-6G", 266),
          ("cellular-gateway-CG418-E", 269),
          ("cellular-gateway-CG522-E", 270),
          ("vedge-IR-1821", 271),
          ("vedge-IR-1831", 272),
          ("vedge-IR-1833", 273),
          ("vedge-IR-1835", 274),
          ("vedge-ISR1100-4GLTEGB-XE", 275),
          ("vedge-ASR-1006-X", 276),
          ("vedge-C1121-8PLTEWK", 277),
          ("vedge-C1117-4PLTELAWZ", 278),
          ("vedge-C8200L-1N-4T", 279),
          ("vedge-C8500-20X6C", 280),
          ("vedge-ESR-6300-NCP", 288),
          ("vedge-ESR-6300-LIC", 289),
          ("vedge-C8330-6TM4SX", 290),
          ("vedge-C8330X-6TM4SX", 291),
          ("vedge-C8330-1N1S-4M2X", 292))
    )


_SystemStatusModel_Type.__name__ = "Integer32"
_SystemStatusModel_Object = MibScalar
systemStatusModel = _SystemStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 47),
    _SystemStatusModel_Type()
)
systemStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusModel.setStatus("current")
_SystemStatusRebootType_Type = String
_SystemStatusRebootType_Object = MibScalar
systemStatusRebootType = _SystemStatusRebootType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 48),
    _SystemStatusRebootType_Type()
)
systemStatusRebootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusRebootType.setStatus("current")
_SystemStatusTotalCpuCount_Type = Unsigned32
_SystemStatusTotalCpuCount_Object = MibScalar
systemStatusTotalCpuCount = _SystemStatusTotalCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 49),
    _SystemStatusTotalCpuCount_Type()
)
systemStatusTotalCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusTotalCpuCount.setStatus("current")
_SystemStatusFpCpuCount_Type = Unsigned32
_SystemStatusFpCpuCount_Object = MibScalar
systemStatusFpCpuCount = _SystemStatusFpCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 50),
    _SystemStatusFpCpuCount_Type()
)
systemStatusFpCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusFpCpuCount.setStatus("current")
_SystemStatusLinuxCpuCount_Type = Unsigned32
_SystemStatusLinuxCpuCount_Object = MibScalar
systemStatusLinuxCpuCount = _SystemStatusLinuxCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 51),
    _SystemStatusLinuxCpuCount_Type()
)
systemStatusLinuxCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusLinuxCpuCount.setStatus("current")


class _SystemStatusState_Type(Integer32):
    """Custom type systemStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blkng-green", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_SystemStatusState_Type.__name__ = "Integer32"
_SystemStatusState_Object = MibScalar
systemStatusState = _SystemStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 54),
    _SystemStatusState_Type()
)
systemStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusState.setStatus("current")
_SystemStatusSystemStateDescription_Type = String
_SystemStatusSystemStateDescription_Object = MibScalar
systemStatusSystemStateDescription = _SystemStatusSystemStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 55),
    _SystemStatusSystemStateDescription_Type()
)
systemStatusSystemStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemStateDescription.setStatus("current")


class _SystemStatusSystemFipsMode_Type(Integer32):
    """Custom type systemStatusSystemFipsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_SystemStatusSystemFipsMode_Type.__name__ = "Integer32"
_SystemStatusSystemFipsMode_Object = MibScalar
systemStatusSystemFipsMode = _SystemStatusSystemFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 58),
    _SystemStatusSystemFipsMode_Type()
)
systemStatusSystemFipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemFipsMode.setStatus("current")
_SystemStatusSystemCtrlCompatibility_Type = String
_SystemStatusSystemCtrlCompatibility_Object = MibScalar
systemStatusSystemCtrlCompatibility = _SystemStatusSystemCtrlCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 60),
    _SystemStatusSystemCtrlCompatibility_Type()
)
systemStatusSystemCtrlCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemCtrlCompatibility.setStatus("current")
_SystemStatusSystemTimezone_Type = String
_SystemStatusSystemTimezone_Object = MibScalar
systemStatusSystemTimezone = _SystemStatusSystemTimezone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 61),
    _SystemStatusSystemTimezone_Type()
)
systemStatusSystemTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemTimezone.setStatus("current")
_SystemStatusSystemLiLicenseEnabled_Type = Unsigned32
_SystemStatusSystemLiLicenseEnabled_Object = MibScalar
systemStatusSystemLiLicenseEnabled = _SystemStatusSystemLiLicenseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 63),
    _SystemStatusSystemLiLicenseEnabled_Type()
)
systemStatusSystemLiLicenseEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemLiLicenseEnabled.setStatus("current")
_SystemStatusSystemChassisSerialNumber_Type = String
_SystemStatusSystemChassisSerialNumber_Object = MibScalar
systemStatusSystemChassisSerialNumber = _SystemStatusSystemChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 64),
    _SystemStatusSystemChassisSerialNumber_Type()
)
systemStatusSystemChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusSystemChassisSerialNumber.setStatus("current")
_SystemStatusInstallerDiskFs_Type = String
_SystemStatusInstallerDiskFs_Object = MibScalar
systemStatusInstallerDiskFs = _SystemStatusInstallerDiskFs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 65),
    _SystemStatusInstallerDiskFs_Type()
)
systemStatusInstallerDiskFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusInstallerDiskFs.setStatus("current")
_SystemStatusInstallerDiskSize_Type = String
_SystemStatusInstallerDiskSize_Object = MibScalar
systemStatusInstallerDiskSize = _SystemStatusInstallerDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 66),
    _SystemStatusInstallerDiskSize_Type()
)
systemStatusInstallerDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusInstallerDiskSize.setStatus("current")
_SystemStatusInstallerDiskUsed_Type = String
_SystemStatusInstallerDiskUsed_Object = MibScalar
systemStatusInstallerDiskUsed = _SystemStatusInstallerDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 67),
    _SystemStatusInstallerDiskUsed_Type()
)
systemStatusInstallerDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusInstallerDiskUsed.setStatus("current")
_SystemStatusInstallerDiskAvail_Type = String
_SystemStatusInstallerDiskAvail_Object = MibScalar
systemStatusInstallerDiskAvail = _SystemStatusInstallerDiskAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 68),
    _SystemStatusInstallerDiskAvail_Type()
)
systemStatusInstallerDiskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusInstallerDiskAvail.setStatus("current")
_SystemStatusInstallerDiskUse_Type = Counter64
_SystemStatusInstallerDiskUse_Object = MibScalar
systemStatusInstallerDiskUse = _SystemStatusInstallerDiskUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 69),
    _SystemStatusInstallerDiskUse_Type()
)
systemStatusInstallerDiskUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusInstallerDiskUse.setStatus("current")
_SystemStatusInstallerDiskMount_Type = String
_SystemStatusInstallerDiskMount_Object = MibScalar
systemStatusInstallerDiskMount = _SystemStatusInstallerDiskMount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 70),
    _SystemStatusInstallerDiskMount_Type()
)
systemStatusInstallerDiskMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusInstallerDiskMount.setStatus("current")
_SystemStatusProductId_Type = String
_SystemStatusProductId_Object = MibScalar
systemStatusProductId = _SystemStatusProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 71),
    _SystemStatusProductId_Type()
)
systemStatusProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusProductId.setStatus("current")
_SystemStatusProcs_Type = Unsigned32
_SystemStatusProcs_Object = MibScalar
systemStatusProcs = _SystemStatusProcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 100),
    _SystemStatusProcs_Type()
)
systemStatusProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusProcs.setStatus("current")
_SystemStatusDiskBsize_Type = Counter64
_SystemStatusDiskBsize_Object = MibScalar
systemStatusDiskBsize = _SystemStatusDiskBsize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 101),
    _SystemStatusDiskBsize_Type()
)
systemStatusDiskBsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBsize.setStatus("current")
_SystemStatusDiskBlocks_Type = Counter64
_SystemStatusDiskBlocks_Object = MibScalar
systemStatusDiskBlocks = _SystemStatusDiskBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 102),
    _SystemStatusDiskBlocks_Type()
)
systemStatusDiskBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBlocks.setStatus("current")
_SystemStatusDiskBused_Type = Counter64
_SystemStatusDiskBused_Object = MibScalar
systemStatusDiskBused = _SystemStatusDiskBused_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 103),
    _SystemStatusDiskBused_Type()
)
systemStatusDiskBused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBused.setStatus("current")
_SystemStatusDiskBavail_Type = Counter64
_SystemStatusDiskBavail_Object = MibScalar
systemStatusDiskBavail = _SystemStatusDiskBavail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 1, 1, 104),
    _SystemStatusDiskBavail_Type()
)
systemStatusDiskBavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemStatusDiskBavail.setStatus("current")
_CiscoSdwanSystemMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoSdwanSystemMIBNotifObjects = _CiscoSdwanSystemMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2)
)
_NetconfNotificationSeverity_Type = NotificationSeverity
_NetconfNotificationSeverity_Object = MibScalar
netconfNotificationSeverity = _NetconfNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 2),
    _NetconfNotificationSeverity_Type()
)
netconfNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netconfNotificationSeverity.setStatus("current")
_CiscoSdwanSystemOldDomainId_Type = DomainId
_CiscoSdwanSystemOldDomainId_Object = MibScalar
ciscoSdwanSystemOldDomainId = _CiscoSdwanSystemOldDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 3),
    _CiscoSdwanSystemOldDomainId_Type()
)
ciscoSdwanSystemOldDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemOldDomainId.setStatus("current")
_CiscoSdwanSystemNewDomainId_Type = DomainId
_CiscoSdwanSystemNewDomainId_Object = MibScalar
ciscoSdwanSystemNewDomainId = _CiscoSdwanSystemNewDomainId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 4),
    _CiscoSdwanSystemNewDomainId_Type()
)
ciscoSdwanSystemNewDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemNewDomainId.setStatus("current")
_CiscoSdwanSystemOldOrganizationName_Type = OctetString
_CiscoSdwanSystemOldOrganizationName_Object = MibScalar
ciscoSdwanSystemOldOrganizationName = _CiscoSdwanSystemOldOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 5),
    _CiscoSdwanSystemOldOrganizationName_Type()
)
ciscoSdwanSystemOldOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemOldOrganizationName.setStatus("current")
_CiscoSdwanSystemNewOrganizationName_Type = OctetString
_CiscoSdwanSystemNewOrganizationName_Object = MibScalar
ciscoSdwanSystemNewOrganizationName = _CiscoSdwanSystemNewOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 6),
    _CiscoSdwanSystemNewOrganizationName_Type()
)
ciscoSdwanSystemNewOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemNewOrganizationName.setStatus("current")
_CiscoSdwanSystemStatusStr_Type = OctetString
_CiscoSdwanSystemStatusStr_Object = MibScalar
ciscoSdwanSystemStatusStr = _CiscoSdwanSystemStatusStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 7),
    _CiscoSdwanSystemStatusStr_Type()
)
ciscoSdwanSystemStatusStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemStatusStr.setStatus("current")
_CiscoSdwanSystemOldSiteId_Type = SiteId
_CiscoSdwanSystemOldSiteId_Object = MibScalar
ciscoSdwanSystemOldSiteId = _CiscoSdwanSystemOldSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 8),
    _CiscoSdwanSystemOldSiteId_Type()
)
ciscoSdwanSystemOldSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemOldSiteId.setStatus("current")
_CiscoSdwanSystemNewSiteId_Type = SiteId
_CiscoSdwanSystemNewSiteId_Object = MibScalar
ciscoSdwanSystemNewSiteId = _CiscoSdwanSystemNewSiteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 9),
    _CiscoSdwanSystemNewSiteId_Type()
)
ciscoSdwanSystemNewSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemNewSiteId.setStatus("current")
_CiscoSdwanSystemUserName_Type = OctetString
_CiscoSdwanSystemUserName_Object = MibScalar
ciscoSdwanSystemUserName = _CiscoSdwanSystemUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 10),
    _CiscoSdwanSystemUserName_Type()
)
ciscoSdwanSystemUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemUserName.setStatus("current")
_CiscoSdwanSystemOldSystemIp_Type = CiscoSdwanIpAddress
_CiscoSdwanSystemOldSystemIp_Object = MibScalar
ciscoSdwanSystemOldSystemIp = _CiscoSdwanSystemOldSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 11),
    _CiscoSdwanSystemOldSystemIp_Type()
)
ciscoSdwanSystemOldSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemOldSystemIp.setStatus("current")
_CiscoSdwanSystemNewSystemIp_Type = CiscoSdwanIpAddress
_CiscoSdwanSystemNewSystemIp_Object = MibScalar
ciscoSdwanSystemNewSystemIp = _CiscoSdwanSystemNewSystemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 2, 12),
    _CiscoSdwanSystemNewSystemIp_Type()
)
ciscoSdwanSystemNewSystemIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSdwanSystemNewSystemIp.setStatus("current")
_CiscoSdwanOperSystemMIBConform_ObjectIdentity = ObjectIdentity
ciscoSdwanOperSystemMIBConform = _CiscoSdwanOperSystemMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 3)
)
_CiscoSdwanOperSystemMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSdwanOperSystemMIBCompliances = _CiscoSdwanOperSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 3, 1)
)
_CiscoSdwanOperSystemMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSdwanOperSystemMIBGroups = _CiscoSdwanOperSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 3, 2)
)

# Managed Objects groups

cSdwanOperSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 3, 2, 1)
)
cSdwanOperSystemGroup.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusPersonality"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusVersion"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskStatus"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusRebootReason"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusUptime"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMin1Avg"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMin5Avg"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMin15Avg"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusCpuUser"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusCpuSystem"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusCpuIdle"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMemTotal"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMemUsed"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMemFree"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMemBuffers"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusMemCached"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskFs"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskSize"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskUsed"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskAvail"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskUse"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskTotalBytes"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskUsedBytes"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskAvailBytes"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskMount"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusServices"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusProcs"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskBsize"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskBlocks"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskBused"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusDiskBavail"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusVmanaged"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusPseudoConfirmCommit"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusConfigTemplateName"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusModel"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusRebootType"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusTotalCpuCount"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusFpCpuCount"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusLinuxCpuCount"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusState"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusSystemStateDescription"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusSystemFipsMode"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusSystemCtrlCompatibility"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusSystemTimezone"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusSystemLiLicenseEnabled"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusSystemChassisSerialNumber"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusInstallerDiskFs"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusInstallerDiskSize"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusInstallerDiskUsed"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusInstallerDiskAvail"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusInstallerDiskUse"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusInstallerDiskMount"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "systemStatusProductId"))
)
if mibBuilder.loadTexts:
    cSdwanOperSystemGroup.setStatus("current")

cSdwanOperSystemNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 3, 2, 2)
)
cSdwanOperSystemNotifObjsGroup.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldDomainId"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewDomainId"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldOrganizationName"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewOrganizationName"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemStatusStr"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldSiteId"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewSiteId"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemUserName"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldSystemIp"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewSystemIp"))
)
if mibBuilder.loadTexts:
    cSdwanOperSystemNotifObjsGroup.setStatus("current")


# Notification objects

ciscoSdwanSystemDomainIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 0, 1)
)
ciscoSdwanSystemDomainIdChange.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldDomainId"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewDomainId"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSystemDomainIdChange.setStatus(
        "current"
    )

ciscoSdwanSystemOrgNameChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 0, 2)
)
ciscoSdwanSystemOrgNameChange.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldOrganizationName"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewOrganizationName"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSystemOrgNameChange.setStatus(
        "current"
    )

ciscoSdwanSystemPseudoCommitStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 0, 3)
)
ciscoSdwanSystemPseudoCommitStatus.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemStatusStr"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSystemPseudoCommitStatus.setStatus(
        "current"
    )

ciscoSdwanSystemSiteIdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 0, 4)
)
ciscoSdwanSystemSiteIdChange.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldSiteId"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewSiteId"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSystemSiteIdChange.setStatus(
        "current"
    )

ciscoSdwanSystemSystemCommit = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 0, 5)
)
ciscoSdwanSystemSystemCommit.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemUserName"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSystemSystemCommit.setStatus(
        "current"
    )

ciscoSdwanSystemSystemIpChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 0, 6)
)
ciscoSdwanSystemSystemIpChange.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "netconfNotificationSeverity"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOldSystemIp"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemNewSystemIp"))
)
if mibBuilder.loadTexts:
    ciscoSdwanSystemSystemIpChange.setStatus(
        "current"
    )


# Notifications groups

cSdwanOperSystemNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 3, 2, 3)
)
cSdwanOperSystemNotifsGroup.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemDomainIdChange"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemOrgNameChange"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemPseudoCommitStatus"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemSiteIdChange"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemSystemCommit"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "ciscoSdwanSystemSystemIpChange"))
)
if mibBuilder.loadTexts:
    cSdwanOperSystemNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSdwanOperSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1004, 3, 1, 1)
)
ciscoSdwanOperSystemMIBCompliance.setObjects(
      *(("CISCO-SDWAN-OPER-SYSTEM-MIB", "cSdwanOperSystemGroup"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "cSdwanOperSystemNotifObjsGroup"),
        ("CISCO-SDWAN-OPER-SYSTEM-MIB", "cSdwanOperSystemNotifsGroup"))
)
if mibBuilder.loadTexts:
    ciscoSdwanOperSystemMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SDWAN-OPER-SYSTEM-MIB",
    **{"String": String,
       "NotificationSeverity": NotificationSeverity,
       "DomainId": DomainId,
       "SiteId": SiteId,
       "CiscoSdwanIpAddress": CiscoSdwanIpAddress,
       "ciscoSdwanOperSystemMIB": ciscoSdwanOperSystemMIB,
       "ciscoSdwanSystemMIBNotifs": ciscoSdwanSystemMIBNotifs,
       "ciscoSdwanSystemDomainIdChange": ciscoSdwanSystemDomainIdChange,
       "ciscoSdwanSystemOrgNameChange": ciscoSdwanSystemOrgNameChange,
       "ciscoSdwanSystemPseudoCommitStatus": ciscoSdwanSystemPseudoCommitStatus,
       "ciscoSdwanSystemSiteIdChange": ciscoSdwanSystemSiteIdChange,
       "ciscoSdwanSystemSystemCommit": ciscoSdwanSystemSystemCommit,
       "ciscoSdwanSystemSystemIpChange": ciscoSdwanSystemSystemIpChange,
       "ciscoSdwanOperSystemMIBObjects": ciscoSdwanOperSystemMIBObjects,
       "systemStatus": systemStatus,
       "systemStatusPersonality": systemStatusPersonality,
       "systemStatusVersion": systemStatusVersion,
       "systemStatusDiskStatus": systemStatusDiskStatus,
       "systemStatusRebootReason": systemStatusRebootReason,
       "systemStatusUptime": systemStatusUptime,
       "systemStatusMin1Avg": systemStatusMin1Avg,
       "systemStatusMin5Avg": systemStatusMin5Avg,
       "systemStatusMin15Avg": systemStatusMin15Avg,
       "systemStatusCpuUser": systemStatusCpuUser,
       "systemStatusCpuSystem": systemStatusCpuSystem,
       "systemStatusCpuIdle": systemStatusCpuIdle,
       "systemStatusMemTotal": systemStatusMemTotal,
       "systemStatusMemUsed": systemStatusMemUsed,
       "systemStatusMemFree": systemStatusMemFree,
       "systemStatusMemBuffers": systemStatusMemBuffers,
       "systemStatusMemCached": systemStatusMemCached,
       "systemStatusDiskFs": systemStatusDiskFs,
       "systemStatusDiskSize": systemStatusDiskSize,
       "systemStatusDiskUsed": systemStatusDiskUsed,
       "systemStatusDiskAvail": systemStatusDiskAvail,
       "systemStatusDiskUse": systemStatusDiskUse,
       "systemStatusDiskTotalBytes": systemStatusDiskTotalBytes,
       "systemStatusDiskUsedBytes": systemStatusDiskUsedBytes,
       "systemStatusDiskAvailBytes": systemStatusDiskAvailBytes,
       "systemStatusDiskMount": systemStatusDiskMount,
       "systemStatusServices": systemStatusServices,
       "systemStatusVmanaged": systemStatusVmanaged,
       "systemStatusPseudoConfirmCommit": systemStatusPseudoConfirmCommit,
       "systemStatusConfigTemplateName": systemStatusConfigTemplateName,
       "systemStatusModel": systemStatusModel,
       "systemStatusRebootType": systemStatusRebootType,
       "systemStatusTotalCpuCount": systemStatusTotalCpuCount,
       "systemStatusFpCpuCount": systemStatusFpCpuCount,
       "systemStatusLinuxCpuCount": systemStatusLinuxCpuCount,
       "systemStatusState": systemStatusState,
       "systemStatusSystemStateDescription": systemStatusSystemStateDescription,
       "systemStatusSystemFipsMode": systemStatusSystemFipsMode,
       "systemStatusSystemCtrlCompatibility": systemStatusSystemCtrlCompatibility,
       "systemStatusSystemTimezone": systemStatusSystemTimezone,
       "systemStatusSystemLiLicenseEnabled": systemStatusSystemLiLicenseEnabled,
       "systemStatusSystemChassisSerialNumber": systemStatusSystemChassisSerialNumber,
       "systemStatusInstallerDiskFs": systemStatusInstallerDiskFs,
       "systemStatusInstallerDiskSize": systemStatusInstallerDiskSize,
       "systemStatusInstallerDiskUsed": systemStatusInstallerDiskUsed,
       "systemStatusInstallerDiskAvail": systemStatusInstallerDiskAvail,
       "systemStatusInstallerDiskUse": systemStatusInstallerDiskUse,
       "systemStatusInstallerDiskMount": systemStatusInstallerDiskMount,
       "systemStatusProductId": systemStatusProductId,
       "systemStatusProcs": systemStatusProcs,
       "systemStatusDiskBsize": systemStatusDiskBsize,
       "systemStatusDiskBlocks": systemStatusDiskBlocks,
       "systemStatusDiskBused": systemStatusDiskBused,
       "systemStatusDiskBavail": systemStatusDiskBavail,
       "ciscoSdwanSystemMIBNotifObjects": ciscoSdwanSystemMIBNotifObjects,
       "netconfNotificationSeverity": netconfNotificationSeverity,
       "ciscoSdwanSystemOldDomainId": ciscoSdwanSystemOldDomainId,
       "ciscoSdwanSystemNewDomainId": ciscoSdwanSystemNewDomainId,
       "ciscoSdwanSystemOldOrganizationName": ciscoSdwanSystemOldOrganizationName,
       "ciscoSdwanSystemNewOrganizationName": ciscoSdwanSystemNewOrganizationName,
       "ciscoSdwanSystemStatusStr": ciscoSdwanSystemStatusStr,
       "ciscoSdwanSystemOldSiteId": ciscoSdwanSystemOldSiteId,
       "ciscoSdwanSystemNewSiteId": ciscoSdwanSystemNewSiteId,
       "ciscoSdwanSystemUserName": ciscoSdwanSystemUserName,
       "ciscoSdwanSystemOldSystemIp": ciscoSdwanSystemOldSystemIp,
       "ciscoSdwanSystemNewSystemIp": ciscoSdwanSystemNewSystemIp,
       "ciscoSdwanOperSystemMIBConform": ciscoSdwanOperSystemMIBConform,
       "ciscoSdwanOperSystemMIBCompliances": ciscoSdwanOperSystemMIBCompliances,
       "ciscoSdwanOperSystemMIBCompliance": ciscoSdwanOperSystemMIBCompliance,
       "ciscoSdwanOperSystemMIBGroups": ciscoSdwanOperSystemMIBGroups,
       "cSdwanOperSystemGroup": cSdwanOperSystemGroup,
       "cSdwanOperSystemNotifObjsGroup": cSdwanOperSystemNotifObjsGroup,
       "cSdwanOperSystemNotifsGroup": cSdwanOperSystemNotifsGroup}
)

# SNMP MIB module (CL-PKTC-EUE-USER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PKTC-EUE-USER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(PktcEUETCAdminStatus,
 PktcEUETCAppIdentifier,
 PktcEUETCAppOrgIdentifier,
 PktcEUETCCreds,
 PktcEUETCCredsType,
 PktcEUETCID,
 PktcEUETCIDType,
 PktcEUETCOperStatus,
 PktcEUETCStatusInfo,
 PktcEUETCUsrAppIndexType,
 PktcEUETCUsrElementIndexType) = mibBuilder.importSymbols(
    "CL-PKTC-EUE-TC-MIB",
    "PktcEUETCAdminStatus",
    "PktcEUETCAppIdentifier",
    "PktcEUETCAppOrgIdentifier",
    "PktcEUETCCreds",
    "PktcEUETCCredsType",
    "PktcEUETCID",
    "PktcEUETCIDType",
    "PktcEUETCOperStatus",
    "PktcEUETCStatusInfo",
    "PktcEUETCUsrAppIndexType",
    "PktcEUETCUsrElementIndexType")

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcEUEUserMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4)
)
if mibBuilder.loadTexts:
    pktcEUEUserMIB.setRevisions(
        ("2011-08-05 00:00",
         "2010-06-16 00:00",
         "2008-07-10 00:00",
         "2007-11-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEUEUsrNotification_ObjectIdentity = ObjectIdentity
pktcEUEUsrNotification = _PktcEUEUsrNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 0)
)
_PktcEUEUsrObjects_ObjectIdentity = ObjectIdentity
pktcEUEUsrObjects = _PktcEUEUsrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1)
)
_PktcEUEUsrProfile_ObjectIdentity = ObjectIdentity
pktcEUEUsrProfile = _PktcEUEUsrProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1)
)


class _PktcEUEUsrProfileVersion_Type(SnmpAdminString):
    """Custom type pktcEUEUsrProfileVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_PktcEUEUsrProfileVersion_Type.__name__ = "SnmpAdminString"
_PktcEUEUsrProfileVersion_Object = MibScalar
pktcEUEUsrProfileVersion = _PktcEUEUsrProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 1),
    _PktcEUEUsrProfileVersion_Type()
)
pktcEUEUsrProfileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrProfileVersion.setStatus("current")
_PktcEUEUsrIMPUTable_Object = MibTable
pktcEUEUsrIMPUTable = _PktcEUEUsrIMPUTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUTable.setStatus("current")
_PktcEUEUsrIMPUEntry_Object = MibTableRow
pktcEUEUsrIMPUEntry = _PktcEUEUsrIMPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1)
)
pktcEUEUsrIMPUEntry.setIndexNames(
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUEntry.setStatus("current")
_PktcEUEUsrIMPUIndex_Type = PktcEUETCUsrElementIndexType
_PktcEUEUsrIMPUIndex_Object = MibTableColumn
pktcEUEUsrIMPUIndex = _PktcEUEUsrIMPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 1),
    _PktcEUEUsrIMPUIndex_Type()
)
pktcEUEUsrIMPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUIndex.setStatus("current")


class _PktcEUEUsrIMPUIdType_Type(PktcEUETCIDType):
    """Custom type pktcEUEUsrIMPUIdType based on PktcEUETCIDType"""
    defaultValue = 1


_PktcEUEUsrIMPUIdType_Type.__name__ = "PktcEUETCIDType"
_PktcEUEUsrIMPUIdType_Object = MibTableColumn
pktcEUEUsrIMPUIdType = _PktcEUEUsrIMPUIdType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 2),
    _PktcEUEUsrIMPUIdType_Type()
)
pktcEUEUsrIMPUIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUIdType.setStatus("current")


class _PktcEUEUsrIMPUId_Type(PktcEUETCID):
    """Custom type pktcEUEUsrIMPUId based on PktcEUETCID"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPUId_Type.__name__ = "PktcEUETCID"
_PktcEUEUsrIMPUId_Object = MibTableColumn
pktcEUEUsrIMPUId = _PktcEUEUsrIMPUId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 3),
    _PktcEUEUsrIMPUId_Type()
)
pktcEUEUsrIMPUId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUId.setStatus("current")


class _PktcEUEUsrIMPUIMPIIndexRef_Type(PktcEUETCUsrElementIndexType):
    """Custom type pktcEUEUsrIMPUIMPIIndexRef based on PktcEUETCUsrElementIndexType"""
    defaultValue = 0


_PktcEUEUsrIMPUIMPIIndexRef_Type.__name__ = "PktcEUETCUsrElementIndexType"
_PktcEUEUsrIMPUIMPIIndexRef_Object = MibTableColumn
pktcEUEUsrIMPUIMPIIndexRef = _PktcEUEUsrIMPUIMPIIndexRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 4),
    _PktcEUEUsrIMPUIMPIIndexRef_Type()
)
pktcEUEUsrIMPUIMPIIndexRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUIMPIIndexRef.setStatus("current")


class _PktcEUEUsrIMPUDispInfo_Type(SnmpAdminString):
    """Custom type pktcEUEUsrIMPUDispInfo based on SnmpAdminString"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPUDispInfo_Type.__name__ = "SnmpAdminString"
_PktcEUEUsrIMPUDispInfo_Object = MibTableColumn
pktcEUEUsrIMPUDispInfo = _PktcEUEUsrIMPUDispInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 5),
    _PktcEUEUsrIMPUDispInfo_Type()
)
pktcEUEUsrIMPUDispInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUDispInfo.setStatus("current")


class _PktcEUEUsrIMPUOpIndexRefs_Type(SnmpAdminString):
    """Custom type pktcEUEUsrIMPUOpIndexRefs based on SnmpAdminString"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPUOpIndexRefs_Type.__name__ = "SnmpAdminString"
_PktcEUEUsrIMPUOpIndexRefs_Object = MibTableColumn
pktcEUEUsrIMPUOpIndexRefs = _PktcEUEUsrIMPUOpIndexRefs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 6),
    _PktcEUEUsrIMPUOpIndexRefs_Type()
)
pktcEUEUsrIMPUOpIndexRefs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUOpIndexRefs.setStatus("current")


class _PktcEUEUsrIMPUAdminStat_Type(PktcEUETCAdminStatus):
    """Custom type pktcEUEUsrIMPUAdminStat based on PktcEUETCAdminStatus"""
    defaultValue = 1


_PktcEUEUsrIMPUAdminStat_Type.__name__ = "PktcEUETCAdminStatus"
_PktcEUEUsrIMPUAdminStat_Object = MibTableColumn
pktcEUEUsrIMPUAdminStat = _PktcEUEUsrIMPUAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 7),
    _PktcEUEUsrIMPUAdminStat_Type()
)
pktcEUEUsrIMPUAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUAdminStat.setStatus("current")


class _PktcEUEUsrIMPUAdminStatInfo_Type(PktcEUETCStatusInfo):
    """Custom type pktcEUEUsrIMPUAdminStatInfo based on PktcEUETCStatusInfo"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPUAdminStatInfo_Type.__name__ = "PktcEUETCStatusInfo"
_PktcEUEUsrIMPUAdminStatInfo_Object = MibTableColumn
pktcEUEUsrIMPUAdminStatInfo = _PktcEUEUsrIMPUAdminStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 8),
    _PktcEUEUsrIMPUAdminStatInfo_Type()
)
pktcEUEUsrIMPUAdminStatInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUAdminStatInfo.setStatus("current")
_PktcEUEUsrIMPUOperStat_Type = PktcEUETCOperStatus
_PktcEUEUsrIMPUOperStat_Object = MibTableColumn
pktcEUEUsrIMPUOperStat = _PktcEUEUsrIMPUOperStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 9),
    _PktcEUEUsrIMPUOperStat_Type()
)
pktcEUEUsrIMPUOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUOperStat.setStatus("current")


class _PktcEUEUsrIMPUOperStatInfo_Type(PktcEUETCStatusInfo):
    """Custom type pktcEUEUsrIMPUOperStatInfo based on PktcEUETCStatusInfo"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPUOperStatInfo_Type.__name__ = "PktcEUETCStatusInfo"
_PktcEUEUsrIMPUOperStatInfo_Object = MibTableColumn
pktcEUEUsrIMPUOperStatInfo = _PktcEUEUsrIMPUOperStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 10),
    _PktcEUEUsrIMPUOperStatInfo_Type()
)
pktcEUEUsrIMPUOperStatInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUOperStatInfo.setStatus("current")


class _PktcEUEUsrIMPUSigSecurity_Type(TruthValue):
    """Custom type pktcEUEUsrIMPUSigSecurity based on TruthValue"""
    defaultValue = 1


_PktcEUEUsrIMPUSigSecurity_Type.__name__ = "TruthValue"
_PktcEUEUsrIMPUSigSecurity_Object = MibTableColumn
pktcEUEUsrIMPUSigSecurity = _PktcEUEUsrIMPUSigSecurity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 11),
    _PktcEUEUsrIMPUSigSecurity_Type()
)
pktcEUEUsrIMPUSigSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUSigSecurity.setStatus("current")


class _PktcEUEUsrIMPUAdditionalInfo_Type(SnmpAdminString):
    """Custom type pktcEUEUsrIMPUAdditionalInfo based on SnmpAdminString"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPUAdditionalInfo_Type.__name__ = "SnmpAdminString"
_PktcEUEUsrIMPUAdditionalInfo_Object = MibTableColumn
pktcEUEUsrIMPUAdditionalInfo = _PktcEUEUsrIMPUAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 12),
    _PktcEUEUsrIMPUAdditionalInfo_Type()
)
pktcEUEUsrIMPUAdditionalInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUAdditionalInfo.setStatus("current")
_PktcEUEUsrIMPURowStatus_Type = RowStatus
_PktcEUEUsrIMPURowStatus_Object = MibTableColumn
pktcEUEUsrIMPURowStatus = _PktcEUEUsrIMPURowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 2, 1, 13),
    _PktcEUEUsrIMPURowStatus_Type()
)
pktcEUEUsrIMPURowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPURowStatus.setStatus("current")
_PktcEUEUsrIMPITable_Object = MibTable
pktcEUEUsrIMPITable = _PktcEUEUsrIMPITable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPITable.setStatus("current")
_PktcEUEUsrIMPIEntry_Object = MibTableRow
pktcEUEUsrIMPIEntry = _PktcEUEUsrIMPIEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3, 1)
)
pktcEUEUsrIMPIEntry.setIndexNames(
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIEntry.setStatus("current")
_PktcEUEUsrIMPIIndex_Type = PktcEUETCUsrElementIndexType
_PktcEUEUsrIMPIIndex_Object = MibTableColumn
pktcEUEUsrIMPIIndex = _PktcEUEUsrIMPIIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3, 1, 1),
    _PktcEUEUsrIMPIIndex_Type()
)
pktcEUEUsrIMPIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIIndex.setStatus("current")


class _PktcEUEUsrIMPIIdType_Type(PktcEUETCIDType):
    """Custom type pktcEUEUsrIMPIIdType based on PktcEUETCIDType"""
    defaultValue = 1


_PktcEUEUsrIMPIIdType_Type.__name__ = "PktcEUETCIDType"
_PktcEUEUsrIMPIIdType_Object = MibTableColumn
pktcEUEUsrIMPIIdType = _PktcEUEUsrIMPIIdType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3, 1, 2),
    _PktcEUEUsrIMPIIdType_Type()
)
pktcEUEUsrIMPIIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIIdType.setStatus("current")


class _PktcEUEUsrIMPIId_Type(PktcEUETCID):
    """Custom type pktcEUEUsrIMPIId based on PktcEUETCID"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPIId_Type.__name__ = "PktcEUETCID"
_PktcEUEUsrIMPIId_Object = MibTableColumn
pktcEUEUsrIMPIId = _PktcEUEUsrIMPIId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3, 1, 3),
    _PktcEUEUsrIMPIId_Type()
)
pktcEUEUsrIMPIId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIId.setStatus("current")


class _PktcEUEUsrIMPICredsType_Type(PktcEUETCCredsType):
    """Custom type pktcEUEUsrIMPICredsType based on PktcEUETCCredsType"""
    defaultValue = 2


_PktcEUEUsrIMPICredsType_Type.__name__ = "PktcEUETCCredsType"
_PktcEUEUsrIMPICredsType_Object = MibTableColumn
pktcEUEUsrIMPICredsType = _PktcEUEUsrIMPICredsType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3, 1, 4),
    _PktcEUEUsrIMPICredsType_Type()
)
pktcEUEUsrIMPICredsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPICredsType.setStatus("current")


class _PktcEUEUsrIMPICredentials_Type(PktcEUETCCreds):
    """Custom type pktcEUEUsrIMPICredentials based on PktcEUETCCreds"""
    defaultValue = OctetString("")


_PktcEUEUsrIMPICredentials_Type.__name__ = "PktcEUETCCreds"
_PktcEUEUsrIMPICredentials_Object = MibTableColumn
pktcEUEUsrIMPICredentials = _PktcEUEUsrIMPICredentials_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3, 1, 5),
    _PktcEUEUsrIMPICredentials_Type()
)
pktcEUEUsrIMPICredentials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPICredentials.setStatus("current")
_PktcEUEUsrIMPIRowStatus_Type = RowStatus
_PktcEUEUsrIMPIRowStatus_Object = MibTableColumn
pktcEUEUsrIMPIRowStatus = _PktcEUEUsrIMPIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 3, 1, 6),
    _PktcEUEUsrIMPIRowStatus_Type()
)
pktcEUEUsrIMPIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIRowStatus.setStatus("current")
_PktcEUEUsrAppMapTable_Object = MibTable
pktcEUEUsrAppMapTable = _PktcEUEUsrAppMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapTable.setStatus("current")
_PktcEUEUsrAppMapEntry_Object = MibTableRow
pktcEUEUsrAppMapEntry = _PktcEUEUsrAppMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1)
)
pktcEUEUsrAppMapEntry.setIndexNames(
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIndex"),
    (0, "CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppIndex"),
)
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapEntry.setStatus("current")
_PktcEUEUsrAppMapAppIndex_Type = PktcEUETCUsrAppIndexType
_PktcEUEUsrAppMapAppIndex_Object = MibTableColumn
pktcEUEUsrAppMapAppIndex = _PktcEUEUsrAppMapAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 1),
    _PktcEUEUsrAppMapAppIndex_Type()
)
pktcEUEUsrAppMapAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppIndex.setStatus("current")
_PktcEUEUsrAppMapAppOrgID_Type = PktcEUETCAppOrgIdentifier
_PktcEUEUsrAppMapAppOrgID_Object = MibTableColumn
pktcEUEUsrAppMapAppOrgID = _PktcEUEUsrAppMapAppOrgID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 2),
    _PktcEUEUsrAppMapAppOrgID_Type()
)
pktcEUEUsrAppMapAppOrgID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppOrgID.setStatus("current")
_PktcEUEUsrAppMapAppIdentifier_Type = PktcEUETCAppIdentifier
_PktcEUEUsrAppMapAppIdentifier_Object = MibTableColumn
pktcEUEUsrAppMapAppIdentifier = _PktcEUEUsrAppMapAppIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 3),
    _PktcEUEUsrAppMapAppIdentifier_Type()
)
pktcEUEUsrAppMapAppIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppIdentifier.setStatus("current")


class _PktcEUEUsrAppMapAppIndexRef_Type(PktcEUETCUsrAppIndexType):
    """Custom type pktcEUEUsrAppMapAppIndexRef based on PktcEUETCUsrAppIndexType"""
    defaultValue = 0


_PktcEUEUsrAppMapAppIndexRef_Type.__name__ = "PktcEUETCUsrAppIndexType"
_PktcEUEUsrAppMapAppIndexRef_Object = MibTableColumn
pktcEUEUsrAppMapAppIndexRef = _PktcEUEUsrAppMapAppIndexRef_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 4),
    _PktcEUEUsrAppMapAppIndexRef_Type()
)
pktcEUEUsrAppMapAppIndexRef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppIndexRef.setStatus("current")


class _PktcEUEUsrAppMapAppAdminStat_Type(PktcEUETCAdminStatus):
    """Custom type pktcEUEUsrAppMapAppAdminStat based on PktcEUETCAdminStatus"""
    defaultValue = 1


_PktcEUEUsrAppMapAppAdminStat_Type.__name__ = "PktcEUETCAdminStatus"
_PktcEUEUsrAppMapAppAdminStat_Object = MibTableColumn
pktcEUEUsrAppMapAppAdminStat = _PktcEUEUsrAppMapAppAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 5),
    _PktcEUEUsrAppMapAppAdminStat_Type()
)
pktcEUEUsrAppMapAppAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppAdminStat.setStatus("current")
_PktcEUEUsrAppMapAppAdminStatInfo_Type = PktcEUETCStatusInfo
_PktcEUEUsrAppMapAppAdminStatInfo_Object = MibTableColumn
pktcEUEUsrAppMapAppAdminStatInfo = _PktcEUEUsrAppMapAppAdminStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 6),
    _PktcEUEUsrAppMapAppAdminStatInfo_Type()
)
pktcEUEUsrAppMapAppAdminStatInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppAdminStatInfo.setStatus("current")
_PktcEUEUsrAppMapAppOperStat_Type = PktcEUETCOperStatus
_PktcEUEUsrAppMapAppOperStat_Object = MibTableColumn
pktcEUEUsrAppMapAppOperStat = _PktcEUEUsrAppMapAppOperStat_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 7),
    _PktcEUEUsrAppMapAppOperStat_Type()
)
pktcEUEUsrAppMapAppOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppOperStat.setStatus("current")
_PktcEUEUsrAppMapAppOperStatInfo_Type = PktcEUETCStatusInfo
_PktcEUEUsrAppMapAppOperStatInfo_Object = MibTableColumn
pktcEUEUsrAppMapAppOperStatInfo = _PktcEUEUsrAppMapAppOperStatInfo_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 8),
    _PktcEUEUsrAppMapAppOperStatInfo_Type()
)
pktcEUEUsrAppMapAppOperStatInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapAppOperStatInfo.setStatus("current")
_PktcEUEUsrAppMapRowStatus_Type = RowStatus
_PktcEUEUsrAppMapRowStatus_Object = MibTableColumn
pktcEUEUsrAppMapRowStatus = _PktcEUEUsrAppMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 1, 1, 4, 1, 9),
    _PktcEUEUsrAppMapRowStatus_Type()
)
pktcEUEUsrAppMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapRowStatus.setStatus("current")
_PktcEUEUsrConformance_ObjectIdentity = ObjectIdentity
pktcEUEUsrConformance = _PktcEUEUsrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2)
)
_PktcEUEUsrCompliances_ObjectIdentity = ObjectIdentity
pktcEUEUsrCompliances = _PktcEUEUsrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 1)
)
_PktcEUEUsrGroups_ObjectIdentity = ObjectIdentity
pktcEUEUsrGroups = _PktcEUEUsrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 2)
)

# Managed Objects groups

pktcEUEUsrProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 2, 1)
)
pktcEUEUsrProfileGroup.setObjects(
    ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrProfileVersion")
)
if mibBuilder.loadTexts:
    pktcEUEUsrProfileGroup.setStatus("current")

pktcEUEUsrIMPUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 2, 2)
)
pktcEUEUsrIMPUGroup.setObjects(
      *(("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIdType"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUId"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUIMPIIndexRef"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUDispInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUOpIndexRefs"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUAdminStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUAdminStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUOperStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUOperStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUSigSecurity"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUAdditionalInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPURowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPUGroup.setStatus("current")

pktcEUEUsrIMPIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 2, 3)
)
pktcEUEUsrIMPIGroup.setObjects(
      *(("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPICredsType"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPICredentials"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIIdType"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIId"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEUsrIMPIGroup.setStatus("current")

pktcEUEUsrAppMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 2, 4)
)
pktcEUEUsrAppMapGroup.setObjects(
      *(("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppOrgID"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppIdentifier"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppIndexRef"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppAdminStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppAdminStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppOperStat"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapAppOperStatInfo"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapRowStatus"))
)
if mibBuilder.loadTexts:
    pktcEUEUsrAppMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEUEUsrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 4, 2, 1, 1)
)
pktcEUEUsrMIBCompliance.setObjects(
      *(("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrProfileGroup"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPUGroup"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrIMPIGroup"),
        ("CL-PKTC-EUE-USER-MIB", "pktcEUEUsrAppMapGroup"))
)
if mibBuilder.loadTexts:
    pktcEUEUsrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-USER-MIB",
    **{"pktcEUEUserMIB": pktcEUEUserMIB,
       "pktcEUEUsrNotification": pktcEUEUsrNotification,
       "pktcEUEUsrObjects": pktcEUEUsrObjects,
       "pktcEUEUsrProfile": pktcEUEUsrProfile,
       "pktcEUEUsrProfileVersion": pktcEUEUsrProfileVersion,
       "pktcEUEUsrIMPUTable": pktcEUEUsrIMPUTable,
       "pktcEUEUsrIMPUEntry": pktcEUEUsrIMPUEntry,
       "pktcEUEUsrIMPUIndex": pktcEUEUsrIMPUIndex,
       "pktcEUEUsrIMPUIdType": pktcEUEUsrIMPUIdType,
       "pktcEUEUsrIMPUId": pktcEUEUsrIMPUId,
       "pktcEUEUsrIMPUIMPIIndexRef": pktcEUEUsrIMPUIMPIIndexRef,
       "pktcEUEUsrIMPUDispInfo": pktcEUEUsrIMPUDispInfo,
       "pktcEUEUsrIMPUOpIndexRefs": pktcEUEUsrIMPUOpIndexRefs,
       "pktcEUEUsrIMPUAdminStat": pktcEUEUsrIMPUAdminStat,
       "pktcEUEUsrIMPUAdminStatInfo": pktcEUEUsrIMPUAdminStatInfo,
       "pktcEUEUsrIMPUOperStat": pktcEUEUsrIMPUOperStat,
       "pktcEUEUsrIMPUOperStatInfo": pktcEUEUsrIMPUOperStatInfo,
       "pktcEUEUsrIMPUSigSecurity": pktcEUEUsrIMPUSigSecurity,
       "pktcEUEUsrIMPUAdditionalInfo": pktcEUEUsrIMPUAdditionalInfo,
       "pktcEUEUsrIMPURowStatus": pktcEUEUsrIMPURowStatus,
       "pktcEUEUsrIMPITable": pktcEUEUsrIMPITable,
       "pktcEUEUsrIMPIEntry": pktcEUEUsrIMPIEntry,
       "pktcEUEUsrIMPIIndex": pktcEUEUsrIMPIIndex,
       "pktcEUEUsrIMPIIdType": pktcEUEUsrIMPIIdType,
       "pktcEUEUsrIMPIId": pktcEUEUsrIMPIId,
       "pktcEUEUsrIMPICredsType": pktcEUEUsrIMPICredsType,
       "pktcEUEUsrIMPICredentials": pktcEUEUsrIMPICredentials,
       "pktcEUEUsrIMPIRowStatus": pktcEUEUsrIMPIRowStatus,
       "pktcEUEUsrAppMapTable": pktcEUEUsrAppMapTable,
       "pktcEUEUsrAppMapEntry": pktcEUEUsrAppMapEntry,
       "pktcEUEUsrAppMapAppIndex": pktcEUEUsrAppMapAppIndex,
       "pktcEUEUsrAppMapAppOrgID": pktcEUEUsrAppMapAppOrgID,
       "pktcEUEUsrAppMapAppIdentifier": pktcEUEUsrAppMapAppIdentifier,
       "pktcEUEUsrAppMapAppIndexRef": pktcEUEUsrAppMapAppIndexRef,
       "pktcEUEUsrAppMapAppAdminStat": pktcEUEUsrAppMapAppAdminStat,
       "pktcEUEUsrAppMapAppAdminStatInfo": pktcEUEUsrAppMapAppAdminStatInfo,
       "pktcEUEUsrAppMapAppOperStat": pktcEUEUsrAppMapAppOperStat,
       "pktcEUEUsrAppMapAppOperStatInfo": pktcEUEUsrAppMapAppOperStatInfo,
       "pktcEUEUsrAppMapRowStatus": pktcEUEUsrAppMapRowStatus,
       "pktcEUEUsrConformance": pktcEUEUsrConformance,
       "pktcEUEUsrCompliances": pktcEUEUsrCompliances,
       "pktcEUEUsrMIBCompliance": pktcEUEUsrMIBCompliance,
       "pktcEUEUsrGroups": pktcEUEUsrGroups,
       "pktcEUEUsrProfileGroup": pktcEUEUsrProfileGroup,
       "pktcEUEUsrIMPUGroup": pktcEUEUsrIMPUGroup,
       "pktcEUEUsrIMPIGroup": pktcEUEUsrIMPIGroup,
       "pktcEUEUsrAppMapGroup": pktcEUEUsrAppMapGroup}
)

# SNMP MIB module (TIMETRA-IPSEC-STATIC-SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-IPSEC-STATIC-SA-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:44:24 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRObjs")

(TNamedItem,
 TNamedItemOrEmpty) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TNamedItemOrEmpty")


# MODULE-IDENTITY

timetraIPsecStaticSAMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 73)
)
if mibBuilder.loadTexts:
    timetraIPsecStaticSAMIBModule.setRevisions(
        ("1909-12-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxAuthAlgorithm(TextualConvention, Integer32):
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
        *(("null", 1),
          ("md5", 2),
          ("sha1", 3))
    )



class TmnxIPsecDirection2(TextualConvention, Integer32):
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
        *(("inbound", 1),
          ("outbound", 2),
          ("bidirectional", 3))
    )



class TmnxIPsecProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 1),
          ("esp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxIPsecStaticSAConformance_ObjectIdentity = ObjectIdentity
tmnxIPsecStaticSAConformance = _TmnxIPsecStaticSAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73)
)
_TmnxIPsecStaticSACompliances_ObjectIdentity = ObjectIdentity
tmnxIPsecStaticSACompliances = _TmnxIPsecStaticSACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1)
)
_TmnxIPsecStaticSAGroups_ObjectIdentity = ObjectIdentity
tmnxIPsecStaticSAGroups = _TmnxIPsecStaticSAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2)
)
_TmnxIPsecStaticSAObjects_ObjectIdentity = ObjectIdentity
tmnxIPsecStaticSAObjects = _TmnxIPsecStaticSAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73)
)
_TmnxIPsecStaticSATableLastChange_Type = TimeStamp
_TmnxIPsecStaticSATableLastChange_Object = MibScalar
tmnxIPsecStaticSATableLastChange = _TmnxIPsecStaticSATableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 1),
    _TmnxIPsecStaticSATableLastChange_Type()
)
tmnxIPsecStaticSATableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSATableLastChange.setStatus("current")
_TmnxIPsecStaticSATable_Object = MibTable
tmnxIPsecStaticSATable = _TmnxIPsecStaticSATable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2)
)
if mibBuilder.loadTexts:
    tmnxIPsecStaticSATable.setStatus("current")
_TmnxIPsecStaticSAEntry_Object = MibTableRow
tmnxIPsecStaticSAEntry = _TmnxIPsecStaticSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1)
)
tmnxIPsecStaticSAEntry.setIndexNames(
    (1, "TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAName"),
)
if mibBuilder.loadTexts:
    tmnxIPsecStaticSAEntry.setStatus("current")
_TmnxIPsecStaticSAName_Type = TNamedItem
_TmnxIPsecStaticSAName_Object = MibTableColumn
tmnxIPsecStaticSAName = _TmnxIPsecStaticSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 1),
    _TmnxIPsecStaticSAName_Type()
)
tmnxIPsecStaticSAName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSAName.setStatus("current")
_TmnxIPsecStaticSARowStatus_Type = RowStatus
_TmnxIPsecStaticSARowStatus_Object = MibTableColumn
tmnxIPsecStaticSARowStatus = _TmnxIPsecStaticSARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 2),
    _TmnxIPsecStaticSARowStatus_Type()
)
tmnxIPsecStaticSARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSARowStatus.setStatus("current")
_TmnxIPsecStaticSALastChanged_Type = TimeStamp
_TmnxIPsecStaticSALastChanged_Object = MibTableColumn
tmnxIPsecStaticSALastChanged = _TmnxIPsecStaticSALastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 3),
    _TmnxIPsecStaticSALastChanged_Type()
)
tmnxIPsecStaticSALastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSALastChanged.setStatus("current")


class _TmnxIPsecStaticSADirection_Type(TmnxIPsecDirection2):
    """Custom type tmnxIPsecStaticSADirection based on TmnxIPsecDirection2"""
    defaultValue = 3


_TmnxIPsecStaticSADirection_Type.__name__ = "TmnxIPsecDirection2"
_TmnxIPsecStaticSADirection_Object = MibTableColumn
tmnxIPsecStaticSADirection = _TmnxIPsecStaticSADirection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 4),
    _TmnxIPsecStaticSADirection_Type()
)
tmnxIPsecStaticSADirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSADirection.setStatus("current")


class _TmnxIPsecStaticSAProtocol_Type(TmnxIPsecProtocol):
    """Custom type tmnxIPsecStaticSAProtocol based on TmnxIPsecProtocol"""
    defaultValue = 2


_TmnxIPsecStaticSAProtocol_Type.__name__ = "TmnxIPsecProtocol"
_TmnxIPsecStaticSAProtocol_Object = MibTableColumn
tmnxIPsecStaticSAProtocol = _TmnxIPsecStaticSAProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 5),
    _TmnxIPsecStaticSAProtocol_Type()
)
tmnxIPsecStaticSAProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSAProtocol.setStatus("current")


class _TmnxIPsecStaticSAAuthAlgorithm_Type(TmnxAuthAlgorithm):
    """Custom type tmnxIPsecStaticSAAuthAlgorithm based on TmnxAuthAlgorithm"""
    defaultValue = 3


_TmnxIPsecStaticSAAuthAlgorithm_Type.__name__ = "TmnxAuthAlgorithm"
_TmnxIPsecStaticSAAuthAlgorithm_Object = MibTableColumn
tmnxIPsecStaticSAAuthAlgorithm = _TmnxIPsecStaticSAAuthAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 6),
    _TmnxIPsecStaticSAAuthAlgorithm_Type()
)
tmnxIPsecStaticSAAuthAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSAAuthAlgorithm.setStatus("current")


class _TmnxIPsecStaticSAAuthKey_Type(OctetString):
    """Custom type tmnxIPsecStaticSAAuthKey based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TmnxIPsecStaticSAAuthKey_Type.__name__ = "OctetString"
_TmnxIPsecStaticSAAuthKey_Object = MibTableColumn
tmnxIPsecStaticSAAuthKey = _TmnxIPsecStaticSAAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 7),
    _TmnxIPsecStaticSAAuthKey_Type()
)
tmnxIPsecStaticSAAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSAAuthKey.setStatus("current")


class _TmnxIPsecStaticSASpi_Type(Unsigned32):
    """Custom type tmnxIPsecStaticSASpi based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(256, 16383),
    )


_TmnxIPsecStaticSASpi_Type.__name__ = "Unsigned32"
_TmnxIPsecStaticSASpi_Object = MibTableColumn
tmnxIPsecStaticSASpi = _TmnxIPsecStaticSASpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 8),
    _TmnxIPsecStaticSASpi_Type()
)
tmnxIPsecStaticSASpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSASpi.setStatus("current")


class _TmnxIPsecStaticSADescription_Type(TNamedItemOrEmpty):
    """Custom type tmnxIPsecStaticSADescription based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxIPsecStaticSADescription_Type.__name__ = "TNamedItemOrEmpty"
_TmnxIPsecStaticSADescription_Object = MibTableColumn
tmnxIPsecStaticSADescription = _TmnxIPsecStaticSADescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 9),
    _TmnxIPsecStaticSADescription_Type()
)
tmnxIPsecStaticSADescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxIPsecStaticSADescription.setStatus("current")

# Managed Objects groups

tmnxIPsecStaticSAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2, 1)
)
tmnxIPsecStaticSAGroup.setObjects(
      *(("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSATableLastChange"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSARowStatus"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSALastChanged"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADirection"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAProtocol"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthAlgorithm"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthKey"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSASpi"),
        ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADescription"))
)
if mibBuilder.loadTexts:
    tmnxIPsecStaticSAGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxIPsecStaticSAV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1, 1)
)
tmnxIPsecStaticSAV8v0Compliance.setObjects(
    ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAGroup")
)
if mibBuilder.loadTexts:
    tmnxIPsecStaticSAV8v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-IPSEC-STATIC-SA-MIB",
    **{"TmnxAuthAlgorithm": TmnxAuthAlgorithm,
       "TmnxIPsecDirection2": TmnxIPsecDirection2,
       "TmnxIPsecProtocol": TmnxIPsecProtocol,
       "timetraIPsecStaticSAMIBModule": timetraIPsecStaticSAMIBModule,
       "tmnxIPsecStaticSAConformance": tmnxIPsecStaticSAConformance,
       "tmnxIPsecStaticSACompliances": tmnxIPsecStaticSACompliances,
       "tmnxIPsecStaticSAV8v0Compliance": tmnxIPsecStaticSAV8v0Compliance,
       "tmnxIPsecStaticSAGroups": tmnxIPsecStaticSAGroups,
       "tmnxIPsecStaticSAGroup": tmnxIPsecStaticSAGroup,
       "tmnxIPsecStaticSAObjects": tmnxIPsecStaticSAObjects,
       "tmnxIPsecStaticSATableLastChange": tmnxIPsecStaticSATableLastChange,
       "tmnxIPsecStaticSATable": tmnxIPsecStaticSATable,
       "tmnxIPsecStaticSAEntry": tmnxIPsecStaticSAEntry,
       "tmnxIPsecStaticSAName": tmnxIPsecStaticSAName,
       "tmnxIPsecStaticSARowStatus": tmnxIPsecStaticSARowStatus,
       "tmnxIPsecStaticSALastChanged": tmnxIPsecStaticSALastChanged,
       "tmnxIPsecStaticSADirection": tmnxIPsecStaticSADirection,
       "tmnxIPsecStaticSAProtocol": tmnxIPsecStaticSAProtocol,
       "tmnxIPsecStaticSAAuthAlgorithm": tmnxIPsecStaticSAAuthAlgorithm,
       "tmnxIPsecStaticSAAuthKey": tmnxIPsecStaticSAAuthKey,
       "tmnxIPsecStaticSASpi": tmnxIPsecStaticSASpi,
       "tmnxIPsecStaticSADescription": tmnxIPsecStaticSADescription}
)

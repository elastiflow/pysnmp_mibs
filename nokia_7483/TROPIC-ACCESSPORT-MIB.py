# SNMP MIB module (TROPIC-ACCESSPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_7483/TROPIC-ACCESSPORT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 18:06:37 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifEntry",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnAccessPortMIB,
 tnPortModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnAccessPortMIB",
    "tnPortModules")

(AluWdmTnIfType,
 TnCommand,
 TropicLEDColorType,
 TropicLEDStateType,
 TropicOperationalCapabilityType,
 TropicStateQualifierType) = mibBuilder.importSymbols(
    "TROPIC-TC",
    "AluWdmTnIfType",
    "TnCommand",
    "TropicLEDColorType",
    "TropicLEDStateType",
    "TropicOperationalCapabilityType",
    "TropicStateQualifierType")


# MODULE-IDENTITY

tnAccessPortMibModules = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    tnAccessPortMibModules.setRevisions(
        ("2008-03-10 12:00",
         "2008-03-20 12:00",
         "2009-02-11 12:00",
         "2009-03-03 12:00",
         "2009-03-03 12:00",
         "2009-03-10 12:00",
         "2009-03-22 12:00",
         "2009-03-31 12:00",
         "2009-06-07 12:00",
         "2009-07-08 12:00",
         "2009-07-10 12:00",
         "2009-11-01 12:00",
         "2010-01-04 12:00",
         "2010-01-15 12:00",
         "2010-05-10 12:00",
         "2010-06-04 12:00",
         "2010-06-28 12:00",
         "2010-09-20 12:00",
         "2010-10-19 12:00",
         "2011-09-30 12:00",
         "2011-11-16 12:00",
         "2012-02-28 12:00",
         "2012-04-25 12:00",
         "2012-08-06 12:00",
         "2012-09-06 12:00",
         "2012-09-27 12:00",
         "2012-12-17 12:00",
         "2013-03-15 12:00",
         "2013-04-12 12:00",
         "2013-05-21 12:00",
         "2013-06-13 12:00",
         "2014-02-26 12:00",
         "2014-03-18 12:00",
         "2014-05-18 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnAccessPortConf_ObjectIdentity = ObjectIdentity
tnAccessPortConf = _TnAccessPortConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1)
)
_TnAccessPortGroups_ObjectIdentity = ObjectIdentity
tnAccessPortGroups = _TnAccessPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1)
)
_TnAccessPortCompliances_ObjectIdentity = ObjectIdentity
tnAccessPortCompliances = _TnAccessPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 2)
)
_TnAccessPortObjs_ObjectIdentity = ObjectIdentity
tnAccessPortObjs = _TnAccessPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2)
)
_TnAccessPortTable_Object = MibTable
tnAccessPortTable = _TnAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnAccessPortTable.setStatus("current")
_TnAccessPortEntry_Object = MibTableRow
tnAccessPortEntry = _TnAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1)
)
tnAccessPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnAccessPortEntry.setStatus("current")


class _TnAccessPortDescr_Type(SnmpAdminString):
    """Custom type tnAccessPortDescr based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnAccessPortDescr_Type.__name__ = "SnmpAdminString"
_TnAccessPortDescr_Object = MibTableColumn
tnAccessPortDescr = _TnAccessPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 1),
    _TnAccessPortDescr_Type()
)
tnAccessPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortDescr.setStatus("current")
_TnAccessPortStatusLEDColor_Type = TropicLEDColorType
_TnAccessPortStatusLEDColor_Object = MibTableColumn
tnAccessPortStatusLEDColor = _TnAccessPortStatusLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 2),
    _TnAccessPortStatusLEDColor_Type()
)
tnAccessPortStatusLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortStatusLEDColor.setStatus("current")
_TnAccessPortStatusLEDState_Type = TropicLEDStateType
_TnAccessPortStatusLEDState_Object = MibTableColumn
tnAccessPortStatusLEDState = _TnAccessPortStatusLEDState_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 3),
    _TnAccessPortStatusLEDState_Type()
)
tnAccessPortStatusLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortStatusLEDState.setStatus("current")


class _TnAccessPortOperationalCapability_Type(TropicOperationalCapabilityType):
    """Custom type tnAccessPortOperationalCapability based on TropicOperationalCapabilityType"""
    defaultValue = 1


_TnAccessPortOperationalCapability_Type.__name__ = "TropicOperationalCapabilityType"
_TnAccessPortOperationalCapability_Object = MibTableColumn
tnAccessPortOperationalCapability = _TnAccessPortOperationalCapability_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 4),
    _TnAccessPortOperationalCapability_Type()
)
tnAccessPortOperationalCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortOperationalCapability.setStatus("current")


class _TnAccessPortStateQualifier_Type(TropicStateQualifierType):
    """Custom type tnAccessPortStateQualifier based on TropicStateQualifierType"""
    defaultHexValue = ""


_TnAccessPortStateQualifier_Type.__name__ = "TropicStateQualifierType"
_TnAccessPortStateQualifier_Object = MibTableColumn
tnAccessPortStateQualifier = _TnAccessPortStateQualifier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 5),
    _TnAccessPortStateQualifier_Type()
)
tnAccessPortStateQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortStateQualifier.setStatus("current")


class _TnAccessPortFarEndAddress_Type(SnmpAdminString):
    """Custom type tnAccessPortFarEndAddress based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnAccessPortFarEndAddress_Type.__name__ = "SnmpAdminString"
_TnAccessPortFarEndAddress_Object = MibTableColumn
tnAccessPortFarEndAddress = _TnAccessPortFarEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 6),
    _TnAccessPortFarEndAddress_Type()
)
tnAccessPortFarEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndAddress.setStatus("current")


class _TnAccessPortFarEndIfIndex_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortFarEndIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortFarEndIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortFarEndIfIndex_Object = MibTableColumn
tnAccessPortFarEndIfIndex = _TnAccessPortFarEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 7),
    _TnAccessPortFarEndIfIndex_Type()
)
tnAccessPortFarEndIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndIfIndex.setStatus("current")


class _TnAccessPortFarEndType_Type(Integer32):
    """Custom type tnAccessPortFarEndType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("internal", 2),
          ("external", 3),
          ("interCompound", 5))
    )


_TnAccessPortFarEndType_Type.__name__ = "Integer32"
_TnAccessPortFarEndType_Object = MibTableColumn
tnAccessPortFarEndType = _TnAccessPortFarEndType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 8),
    _TnAccessPortFarEndType_Type()
)
tnAccessPortFarEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndType.setStatus("current")


class _TnAccessPortDirection_Type(Integer32):
    """Custom type tnAccessPortDirection based on Integer32"""
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
        *(("bidirectional", 1),
          ("unidirectionalTx", 2),
          ("unidirectionalRx", 3))
    )


_TnAccessPortDirection_Type.__name__ = "Integer32"
_TnAccessPortDirection_Object = MibTableColumn
tnAccessPortDirection = _TnAccessPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 9),
    _TnAccessPortDirection_Type()
)
tnAccessPortDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortDirection.setStatus("current")
_TnAccessPortAINS_Type = TruthValue
_TnAccessPortAINS_Object = MibTableColumn
tnAccessPortAINS = _TnAccessPortAINS_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 10),
    _TnAccessPortAINS_Type()
)
tnAccessPortAINS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortAINS.setStatus("current")


class _TnAccessPortAINSDebounceTime_Type(Integer32):
    """Custom type tnAccessPortAINSDebounceTime based on Integer32"""
    defaultValue = -1


_TnAccessPortAINSDebounceTime_Type.__name__ = "Integer32"
_TnAccessPortAINSDebounceTime_Object = MibTableColumn
tnAccessPortAINSDebounceTime = _TnAccessPortAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 11),
    _TnAccessPortAINSDebounceTime_Type()
)
tnAccessPortAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTime.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTime.setUnits("seconds")
_TnAccessPortUsingSysAINSDebounceTime_Type = TruthValue
_TnAccessPortUsingSysAINSDebounceTime_Object = MibTableColumn
tnAccessPortUsingSysAINSDebounceTime = _TnAccessPortUsingSysAINSDebounceTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 12),
    _TnAccessPortUsingSysAINSDebounceTime_Type()
)
tnAccessPortUsingSysAINSDebounceTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortUsingSysAINSDebounceTime.setStatus("current")


class _TnAccessPortAINSDebounceTimeRemaining_Type(Unsigned32):
    """Custom type tnAccessPortAINSDebounceTimeRemaining based on Unsigned32"""
    defaultValue = 0


_TnAccessPortAINSDebounceTimeRemaining_Type.__name__ = "Unsigned32"
_TnAccessPortAINSDebounceTimeRemaining_Object = MibTableColumn
tnAccessPortAINSDebounceTimeRemaining = _TnAccessPortAINSDebounceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 13),
    _TnAccessPortAINSDebounceTimeRemaining_Type()
)
tnAccessPortAINSDebounceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessPortAINSDebounceTimeRemaining.setUnits("seconds")


class _TnAccessPortIsDomainEdgePort_Type(TruthValue):
    """Custom type tnAccessPortIsDomainEdgePort based on TruthValue"""
    defaultValue = 1


_TnAccessPortIsDomainEdgePort_Type.__name__ = "TruthValue"
_TnAccessPortIsDomainEdgePort_Object = MibTableColumn
tnAccessPortIsDomainEdgePort = _TnAccessPortIsDomainEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 14),
    _TnAccessPortIsDomainEdgePort_Type()
)
tnAccessPortIsDomainEdgePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortIsDomainEdgePort.setStatus("current")


class _TnAccessPortFarEndAddressConnFrom_Type(SnmpAdminString):
    """Custom type tnAccessPortFarEndAddressConnFrom based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnAccessPortFarEndAddressConnFrom_Type.__name__ = "SnmpAdminString"
_TnAccessPortFarEndAddressConnFrom_Object = MibTableColumn
tnAccessPortFarEndAddressConnFrom = _TnAccessPortFarEndAddressConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 15),
    _TnAccessPortFarEndAddressConnFrom_Type()
)
tnAccessPortFarEndAddressConnFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndAddressConnFrom.setStatus("current")


class _TnAccessPortFarEndIfIndexConnFrom_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortFarEndIfIndexConnFrom based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortFarEndIfIndexConnFrom_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortFarEndIfIndexConnFrom_Object = MibTableColumn
tnAccessPortFarEndIfIndexConnFrom = _TnAccessPortFarEndIfIndexConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 16),
    _TnAccessPortFarEndIfIndexConnFrom_Type()
)
tnAccessPortFarEndIfIndexConnFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndIfIndexConnFrom.setStatus("current")


class _TnAccessPortFarEndTypeConnFrom_Type(Integer32):
    """Custom type tnAccessPortFarEndTypeConnFrom based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 1),
          ("internal", 2),
          ("external", 3),
          ("interCompound", 5))
    )


_TnAccessPortFarEndTypeConnFrom_Type.__name__ = "Integer32"
_TnAccessPortFarEndTypeConnFrom_Object = MibTableColumn
tnAccessPortFarEndTypeConnFrom = _TnAccessPortFarEndTypeConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 17),
    _TnAccessPortFarEndTypeConnFrom_Type()
)
tnAccessPortFarEndTypeConnFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortFarEndTypeConnFrom.setStatus("current")
_TnAccessPortExtAmpIpAddressIn_Type = IpAddress
_TnAccessPortExtAmpIpAddressIn_Object = MibTableColumn
tnAccessPortExtAmpIpAddressIn = _TnAccessPortExtAmpIpAddressIn_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 18),
    _TnAccessPortExtAmpIpAddressIn_Type()
)
tnAccessPortExtAmpIpAddressIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortExtAmpIpAddressIn.setStatus("current")
_TnAccessPortExtAmpIpAddressOut_Type = IpAddress
_TnAccessPortExtAmpIpAddressOut_Object = MibTableColumn
tnAccessPortExtAmpIpAddressOut = _TnAccessPortExtAmpIpAddressOut_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 19),
    _TnAccessPortExtAmpIpAddressOut_Type()
)
tnAccessPortExtAmpIpAddressOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortExtAmpIpAddressOut.setStatus("current")


class _TnAccessPortWtocmConnLoss_Type(Integer32):
    """Custom type tnAccessPortWtocmConnLoss based on Integer32"""
    defaultValue = 0


_TnAccessPortWtocmConnLoss_Type.__name__ = "Integer32"
_TnAccessPortWtocmConnLoss_Object = MibTableColumn
tnAccessPortWtocmConnLoss = _TnAccessPortWtocmConnLoss_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 20),
    _TnAccessPortWtocmConnLoss_Type()
)
tnAccessPortWtocmConnLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortWtocmConnLoss.setStatus("current")
if mibBuilder.loadTexts:
    tnAccessPortWtocmConnLoss.setUnits("mB")


class _TnAccessPortWtocmConnAddress_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortWtocmConnAddress based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortWtocmConnAddress_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortWtocmConnAddress_Object = MibTableColumn
tnAccessPortWtocmConnAddress = _TnAccessPortWtocmConnAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 21),
    _TnAccessPortWtocmConnAddress_Type()
)
tnAccessPortWtocmConnAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortWtocmConnAddress.setStatus("current")


class _TnAccessPortOppDirectionPortAddress_Type(InterfaceIndexOrZero):
    """Custom type tnAccessPortOppDirectionPortAddress based on InterfaceIndexOrZero"""
    defaultValue = 0


_TnAccessPortOppDirectionPortAddress_Type.__name__ = "InterfaceIndexOrZero"
_TnAccessPortOppDirectionPortAddress_Object = MibTableColumn
tnAccessPortOppDirectionPortAddress = _TnAccessPortOppDirectionPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 22),
    _TnAccessPortOppDirectionPortAddress_Type()
)
tnAccessPortOppDirectionPortAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortOppDirectionPortAddress.setStatus("current")


class _TnAccessPortIsValidInternalOTSXcEndpoint_Type(TruthValue):
    """Custom type tnAccessPortIsValidInternalOTSXcEndpoint based on TruthValue"""
    defaultValue = 2


_TnAccessPortIsValidInternalOTSXcEndpoint_Type.__name__ = "TruthValue"
_TnAccessPortIsValidInternalOTSXcEndpoint_Object = MibTableColumn
tnAccessPortIsValidInternalOTSXcEndpoint = _TnAccessPortIsValidInternalOTSXcEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 23),
    _TnAccessPortIsValidInternalOTSXcEndpoint_Type()
)
tnAccessPortIsValidInternalOTSXcEndpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortIsValidInternalOTSXcEndpoint.setStatus("current")


class _TnAccessPortWtDomainNumber_Type(Integer32):
    """Custom type tnAccessPortWtDomainNumber based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 19),
    )


_TnAccessPortWtDomainNumber_Type.__name__ = "Integer32"
_TnAccessPortWtDomainNumber_Object = MibTableColumn
tnAccessPortWtDomainNumber = _TnAccessPortWtDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 24),
    _TnAccessPortWtDomainNumber_Type()
)
tnAccessPortWtDomainNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnAccessPortWtDomainNumber.setStatus("current")
_TnAccessPortHasMpoConnector_Type = TruthValue
_TnAccessPortHasMpoConnector_Object = MibTableColumn
tnAccessPortHasMpoConnector = _TnAccessPortHasMpoConnector_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 25),
    _TnAccessPortHasMpoConnector_Type()
)
tnAccessPortHasMpoConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortHasMpoConnector.setStatus("current")
_TnAccessPortMpoConnectorPortOutIfIndex_Type = InterfaceIndexOrZero
_TnAccessPortMpoConnectorPortOutIfIndex_Object = MibTableColumn
tnAccessPortMpoConnectorPortOutIfIndex = _TnAccessPortMpoConnectorPortOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 26),
    _TnAccessPortMpoConnectorPortOutIfIndex_Type()
)
tnAccessPortMpoConnectorPortOutIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortMpoConnectorPortOutIfIndex.setStatus("current")
_TnAccessPortMpoConnectorPortInIfIndex_Type = InterfaceIndexOrZero
_TnAccessPortMpoConnectorPortInIfIndex_Object = MibTableColumn
tnAccessPortMpoConnectorPortInIfIndex = _TnAccessPortMpoConnectorPortInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 27),
    _TnAccessPortMpoConnectorPortInIfIndex_Type()
)
tnAccessPortMpoConnectorPortInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortMpoConnectorPortInIfIndex.setStatus("current")
_TnAccessPortIsMpo_Type = TruthValue
_TnAccessPortIsMpo_Object = MibTableColumn
tnAccessPortIsMpo = _TnAccessPortIsMpo_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 1, 1, 28),
    _TnAccessPortIsMpo_Type()
)
tnAccessPortIsMpo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnAccessPortIsMpo.setStatus("current")
_TnIfTable_Object = MibTable
tnIfTable = _TnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnIfTable.setStatus("current")
_TnIfEntry_Object = MibTableRow
tnIfEntry = _TnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tnIfEntry.setStatus("current")
_TnIfPhysicalLocation_Type = InterfaceIndex
_TnIfPhysicalLocation_Object = MibTableColumn
tnIfPhysicalLocation = _TnIfPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 1),
    _TnIfPhysicalLocation_Type()
)
tnIfPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfPhysicalLocation.setStatus("current")
_TnIfType_Type = AluWdmTnIfType
_TnIfType_Object = MibTableColumn
tnIfType = _TnIfType_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 2),
    _TnIfType_Type()
)
tnIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIfType.setStatus("current")


class _TnIfSupportedTypes_Type(Bits):
    """Custom type tnIfSupportedTypes based on Bits"""
    namedValues = NamedValues(
        *(("oc3", 0),
          ("oc12", 1),
          ("oc48", 2),
          ("oc192", 3),
          ("ots", 4),
          ("och", 5),
          ("otu1", 6),
          ("otu2", 7),
          ("gige", 8),
          ("tenGige", 9),
          ("stm1", 10),
          ("stm4", 11),
          ("stm16", 12),
          ("stm64", 13),
          ("fc1g", 14),
          ("fc2g", 15),
          ("fc4g", 16),
          ("fc10g", 17),
          ("cbr2g5", 18),
          ("cbr10g", 19),
          ("anyRate", 20),
          ("hdSdi", 21),
          ("fe", 22),
          ("fddi", 23),
          ("esCon", 24),
          ("dvbAsi", 25),
          ("dvi6000", 26),
          ("otu3", 27),
          ("oc768", 28),
          ("stm256", 29),
          ("otu4", 30),
          ("fc8g", 31),
          ("hundredGige", 32),
          ("sdsdi", 33),
          ("e1", 34),
          ("sdi3g", 35),
          ("dcn", 36),
          ("evoa", 37),
          ("fee", 38),
          ("oduptf", 39),
          ("ds1", 40),
          ("otu3e2", 41),
          ("otu2e", 42),
          ("fortyGige", 43),
          ("sdr", 44),
          ("ddr", 45),
          ("tod", 46),
          ("lagGroup", 47),
          ("otl44", 48),
          ("fc16g", 49),
          ("qdr", 50),
          ("bits", 51),
          ("oneTru", 52),
          ("otu4x2", 53),
          ("otu1f", 54),
          ("cbr10g3", 55),
          ("fortyGigeMLD", 56))
    )

_TnIfSupportedTypes_Type.__name__ = "Bits"
_TnIfSupportedTypes_Object = MibTableColumn
tnIfSupportedTypes = _TnIfSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 3),
    _TnIfSupportedTypes_Type()
)
tnIfSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfSupportedTypes.setStatus("current")


class _TnIfSupportedTypesAlternate_Type(OctetString):
    """Custom type tnIfSupportedTypesAlternate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_TnIfSupportedTypesAlternate_Type.__name__ = "OctetString"
_TnIfSupportedTypesAlternate_Object = MibTableColumn
tnIfSupportedTypesAlternate = _TnIfSupportedTypesAlternate_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 4),
    _TnIfSupportedTypesAlternate_Type()
)
tnIfSupportedTypesAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnIfSupportedTypesAlternate.setStatus("current")
_TnIfForceAdminStatus_Type = TnCommand
_TnIfForceAdminStatus_Object = MibTableColumn
tnIfForceAdminStatus = _TnIfForceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 2, 1, 5),
    _TnIfForceAdminStatus_Type()
)
tnIfForceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tnIfForceAdminStatus.setStatus("current")
_TnAccessPortScalarObjs_ObjectIdentity = ObjectIdentity
tnAccessPortScalarObjs = _TnAccessPortScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 3)
)
_TnSysTopology_ObjectIdentity = ObjectIdentity
tnSysTopology = _TnSysTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 3, 1)
)


class _TnSysTopologyAudit_Type(SnmpAdminString):
    """Custom type tnSysTopologyAudit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnSysTopologyAudit_Type.__name__ = "SnmpAdminString"
_TnSysTopologyAudit_Object = MibScalar
tnSysTopologyAudit = _TnSysTopologyAudit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 2, 3, 1, 1),
    _TnSysTopologyAudit_Type()
)
tnSysTopologyAudit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnSysTopologyAudit.setStatus("current")
ifEntry.registerAugmentions(
    ("TROPIC-ACCESSPORT-MIB",
     "tnIfEntry")
)
tnIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

tnAccessPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1, 1)
)
tnAccessPortGroup.setObjects(
      *(("TROPIC-ACCESSPORT-MIB", "tnAccessPortDescr"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortStatusLEDColor"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortStatusLEDState"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortOperationalCapability"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortStateQualifier"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndIfIndex"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndType"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortDirection"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAINS"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAINSDebounceTime"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortUsingSysAINSDebounceTime"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortAINSDebounceTimeRemaining"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortIsDomainEdgePort"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndAddressConnFrom"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndIfIndexConnFrom"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortFarEndTypeConnFrom"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortExtAmpIpAddressIn"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortExtAmpIpAddressOut"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortWtocmConnLoss"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortWtocmConnAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortOppDirectionPortAddress"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortIsValidInternalOTSXcEndpoint"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortWtDomainNumber"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortHasMpoConnector"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortMpoConnectorPortOutIfIndex"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortMpoConnectorPortInIfIndex"),
        ("TROPIC-ACCESSPORT-MIB", "tnAccessPortIsMpo"))
)
if mibBuilder.loadTexts:
    tnAccessPortGroup.setStatus("current")

tnIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1, 2)
)
tnIfGroup.setObjects(
      *(("TROPIC-ACCESSPORT-MIB", "tnIfPhysicalLocation"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfType"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfSupportedTypes"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfSupportedTypesAlternate"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfForceAdminStatus"))
)
if mibBuilder.loadTexts:
    tnIfGroup.setStatus("current")

tnSysTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 1, 3)
)
tnSysTopologyGroup.setObjects(
    ("TROPIC-ACCESSPORT-MIB", "tnSysTopologyAudit")
)
if mibBuilder.loadTexts:
    tnSysTopologyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnAccessPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 1, 1, 2, 1)
)
tnAccessPortCompliance.setObjects(
      *(("TROPIC-ACCESSPORT-MIB", "tnAccessPortGroup"),
        ("TROPIC-ACCESSPORT-MIB", "tnIfGroup"),
        ("TROPIC-ACCESSPORT-MIB", "tnSysTopologyGroup"))
)
if mibBuilder.loadTexts:
    tnAccessPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-ACCESSPORT-MIB",
    **{"tnAccessPortMibModules": tnAccessPortMibModules,
       "tnAccessPortConf": tnAccessPortConf,
       "tnAccessPortGroups": tnAccessPortGroups,
       "tnAccessPortGroup": tnAccessPortGroup,
       "tnIfGroup": tnIfGroup,
       "tnSysTopologyGroup": tnSysTopologyGroup,
       "tnAccessPortCompliances": tnAccessPortCompliances,
       "tnAccessPortCompliance": tnAccessPortCompliance,
       "tnAccessPortObjs": tnAccessPortObjs,
       "tnAccessPortTable": tnAccessPortTable,
       "tnAccessPortEntry": tnAccessPortEntry,
       "tnAccessPortDescr": tnAccessPortDescr,
       "tnAccessPortStatusLEDColor": tnAccessPortStatusLEDColor,
       "tnAccessPortStatusLEDState": tnAccessPortStatusLEDState,
       "tnAccessPortOperationalCapability": tnAccessPortOperationalCapability,
       "tnAccessPortStateQualifier": tnAccessPortStateQualifier,
       "tnAccessPortFarEndAddress": tnAccessPortFarEndAddress,
       "tnAccessPortFarEndIfIndex": tnAccessPortFarEndIfIndex,
       "tnAccessPortFarEndType": tnAccessPortFarEndType,
       "tnAccessPortDirection": tnAccessPortDirection,
       "tnAccessPortAINS": tnAccessPortAINS,
       "tnAccessPortAINSDebounceTime": tnAccessPortAINSDebounceTime,
       "tnAccessPortUsingSysAINSDebounceTime": tnAccessPortUsingSysAINSDebounceTime,
       "tnAccessPortAINSDebounceTimeRemaining": tnAccessPortAINSDebounceTimeRemaining,
       "tnAccessPortIsDomainEdgePort": tnAccessPortIsDomainEdgePort,
       "tnAccessPortFarEndAddressConnFrom": tnAccessPortFarEndAddressConnFrom,
       "tnAccessPortFarEndIfIndexConnFrom": tnAccessPortFarEndIfIndexConnFrom,
       "tnAccessPortFarEndTypeConnFrom": tnAccessPortFarEndTypeConnFrom,
       "tnAccessPortExtAmpIpAddressIn": tnAccessPortExtAmpIpAddressIn,
       "tnAccessPortExtAmpIpAddressOut": tnAccessPortExtAmpIpAddressOut,
       "tnAccessPortWtocmConnLoss": tnAccessPortWtocmConnLoss,
       "tnAccessPortWtocmConnAddress": tnAccessPortWtocmConnAddress,
       "tnAccessPortOppDirectionPortAddress": tnAccessPortOppDirectionPortAddress,
       "tnAccessPortIsValidInternalOTSXcEndpoint": tnAccessPortIsValidInternalOTSXcEndpoint,
       "tnAccessPortWtDomainNumber": tnAccessPortWtDomainNumber,
       "tnAccessPortHasMpoConnector": tnAccessPortHasMpoConnector,
       "tnAccessPortMpoConnectorPortOutIfIndex": tnAccessPortMpoConnectorPortOutIfIndex,
       "tnAccessPortMpoConnectorPortInIfIndex": tnAccessPortMpoConnectorPortInIfIndex,
       "tnAccessPortIsMpo": tnAccessPortIsMpo,
       "tnIfTable": tnIfTable,
       "tnIfEntry": tnIfEntry,
       "tnIfPhysicalLocation": tnIfPhysicalLocation,
       "tnIfType": tnIfType,
       "tnIfSupportedTypes": tnIfSupportedTypes,
       "tnIfSupportedTypesAlternate": tnIfSupportedTypesAlternate,
       "tnIfForceAdminStatus": tnIfForceAdminStatus,
       "tnAccessPortScalarObjs": tnAccessPortScalarObjs,
       "tnSysTopology": tnSysTopology,
       "tnSysTopologyAudit": tnSysTopologyAudit}
)
